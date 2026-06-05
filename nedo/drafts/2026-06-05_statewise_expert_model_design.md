# 6状態別 Expert Model による作業状態推定設計

## Summary

NEDOシステムの作業状態推定は、最初から全モーダルを巨大な深層学習モデルに投入する必要はない。むしろ、以下の6状態それぞれに小さな expert model を置き、各 expert が「その状態らしさの確率」を出し、最後に軽量な統合層で最終ラベルを決める方が、先行研究の成果を組み合わせた設計として説明しやすい。

対象とする6状態:

1. 順調な集中・flow-like
2. 高負荷だが進捗あり
3. 高負荷で停滞
4. 低活動だが思考中
5. 離脱・マインドワンダリング
6. 中断・タスク切替

この設計では、`Z(t)` を巨大な抽象概念として扱わない。実装上は、各時間窓 `t` について、6つの状態 expert が確率を出す。

```text
p_focused(t)     = expert_focused(x_t)
p_highload_work(t)= expert_highload_work(x_t)
p_stuck(t)       = expert_stuck(x_t)
p_thinking(t)    = expert_thinking(x_t)
p_distracted(t)  = expert_distracted(x_t)
p_switching(t)   = expert_switching(x_t)

p(t) = [p_focused, p_highload_work, p_stuck, p_thinking, p_distracted, p_switching]
state(t) = argmax softmax(W p(t) + b)
```

ここで `W` は最終ラベル出力層の重みであり、初期実装では手で決めた重みでもよい。データが集まったら、ロジスティック回帰、温度付きsoftmax、LightGBM、HMMなどで学習する。

## 1. 全体アーキテクチャ

### 1.1 なぜ状態別 expert にするか

各状態は、必要なモーダルが違う。

| 状態 | 主に必要なモーダル | 大きな1モデルにしない理由 |
| --- | --- | --- |
| 順調な集中・flow-like | 操作ログ、進捗、切替少なさ、自己報告 | EEGだけでは過剰。Brown et al. 2023 の focused work 指標を使いやすい。 |
| 高負荷だが進捗あり | EEG/生理信号、成果物変化 | 負荷と進捗を別々に見れば判定できる。 |
| 高負荷で停滞 | EEG/生理信号、エラー反復、進捗低下、画面文脈 | ルールベースでもかなり判定可能。 |
| 低活動だが思考中 | 入力停止、EEG/注意、作業画面維持 | 操作ログだけでは離脱と混同する。 |
| 離脱・マインドワンダリング | 入力停止、作業外画面、低負荷、視線逸脱 | Hamed et al. 2026 の on-screen/on-task 分離に近い。 |
| 中断・タスク切替 | アプリ切替、通知、Todo非関連、画面遷移 | 操作ログ中心で取れる。 |

つまり、6状態は「同じ特徴量を同じように使う6クラス分類」ではない。各状態ごとに、先行研究に対応した異なる小問題として解く方が自然である。

### 1.2 Expert の入力と出力

時間窓 `t` ごとに、次の共通特徴量テーブルを作る。

```text
x_t = [
  eeg_features,
  physio_features,
  action_features,
  screen_features,
  progress_features,
  self_report_features,
  todo_context_features
]
```

各 expert は、このうち必要な特徴だけを使う。

```text
expert_k: x_t_subset -> probability in [0, 1]
```

最終出力は次のJSONにする。

```json
{
  "state_probs": {
    "focused": 0.72,
    "highload_work": 0.41,
    "stuck": 0.08,
    "thinking": 0.23,
    "distracted": 0.04,
    "switching": 0.02
  },
  "state": "focused",
  "expert_evidence": {
    "focused": ["related action session", "low app switching", "progress observed"],
    "stuck": ["workload not high enough", "no repeated error"]
  }
}
```

## 2. Expert 1: 順調な集中・flow-like

### 2.1 解く問題

作業が同じ文脈で継続し、進捗もあり、過度な中断がなく、本人の主観としても悪くない区間を検出する。

ここで重要なのは、心理学的な flow そのものを直接測るのではなく、Brown et al. 2023 が行ったように、まずは focused work をログから推定し、その上に進捗・快/不快・自己報告を重ねて `flow_like` とすることである。

### 2.2 使う先行研究

| 研究 | 借りる部分 |
| --- | --- |
| Brown et al. 2023 | ログから関連行動の連続区間、つまり focus time を推定する発想。Word2Vecでタスク類似度を表し、自己報告と照合する設計。 |
| Müller and Fritz 2015 | 進捗と感情を別軸で扱う発想。 |
| Kevic et al. 2015 | 視線/操作が作業対象へ向いているかを見る補助。 |

### 2.3 入力特徴量

| feature | 意味 |
| --- | --- |
| `related_action_session_score` | Brown et al. 2023風の、同一/関連タスク行動が続いている度合い |
| `app_switch_count` | アプリ切替回数 |
| `unrelated_app_seconds` | Todoと関係ない画面時間 |
| `git_lines_changed` | 成果物変化 |
| `task_completion_event` | Todo完了、テスト通過、ビルド成功など |
| `self_report_focus` | 作業後の集中自己報告 |
| `self_report_valence` | 快/不快 |
| `workload_score` | 高すぎない認知負荷 |

### 2.4 最初の算出方法

```text
p_focused =
  sigmoid(
    + 1.5 * related_action_session_score
    + 1.0 * progress_score
    + 0.8 * self_report_focus
    + 0.5 * self_report_valence
    - 1.0 * context_switch_score
    - 0.7 * overload_score
  )
```

自己報告がないリアルタイム推定では、`self_report_*` を欠損として扱い、残りで近似する。

```text
p_focused_realtime =
  sigmoid(
    + related_action_session_score
    + progress_score
    - context_switch_score
    - stuck_score
  )
```

### 2.5 評価

- diary/retrospective self-report の focused work との一致
- `flow_like` は flow 本体ではなく、focused work + 進捗 + 主観良好の proxy と明記する
- Brown et al. 2023 のように、自己報告との一致率や PABAK 的な一致指標を参考にする

## 3. Expert 2: 高負荷だが進捗あり

### 3.1 解く問題

認知負荷は高いが、作業成果は出ている状態を検出する。これは、支援や割り込みを必ずしも必要としない。むしろ「難しいが前に進んでいる」状態として、作業レポートに記録するべきである。

### 3.2 使う先行研究

| 研究 | 借りる部分 |
| --- | --- |
| Fritz et al. 2014 | EEG/視線/EDAでソフトウェア作業の難易度を分類する発想。 |
| CLARE 2024 | ECG/EDA/EEG/視線と自己報告負荷を用いた負荷推定、10-fold/LOSO評価。 |
| CL-Drive 2024 | 現実的操作課題での多モーダル認知負荷分類。 |
| Müller and Fritz 2015 | 低/高進捗を別軸で分類する発想。 |

### 3.3 入力特徴量

| feature | 意味 |
| --- | --- |
| `eeg_workload_score` | EEG由来の負荷推定 |
| `eda_arousal_score` | EDA由来の覚醒/負荷 |
| `pupil_dilation_score` | 瞳孔由来の負荷 |
| `gaze_fixation_intensity` | 注視集中度 |
| `git_lines_changed` | 成果物変化 |
| `test_success_event` | テスト/ビルド成功 |
| `screen_error_repetition` | 同じエラーの反復 |
| `self_report_workload` | 負荷自己報告 |
| `self_report_progress` | 進捗自己報告 |

### 3.4 最初の算出方法

```text
workload_score =
  calibrated_model_eeg_physio(X_eeg, X_eda, X_ecg, X_pupil)

progress_score =
  normalize(
    git_lines_changed
    + task_completion_event
    + test_success_event
    - repeated_error_penalty
  )

p_highload_work =
  workload_score * progress_score * (1 - stuck_penalty)
```

`workload_score` は、最初は EEG の周波数特徴 + EDA/ECG の軽量分類器でよい。分類器候補は Logistic Regression、Random Forest、LightGBM。CLARE/CL-Driveのように、個人内評価とLOSO評価を分ける。

### 3.5 評価

- 自己報告の workload と相関するか
- 進捗自己報告や成果物変化と一致するか
- `高負荷で停滞` と混同しないか

## 4. Expert 3: 高負荷で停滞

### 4.1 解く問題

認知負荷が高く、かつ進捗が出ていない状態を検出する。この状態は、タスク細分化エージェントが最も介入しやすい。

### 4.2 使う先行研究

| 研究 | 借りる部分 |
| --- | --- |
| Fritz et al. 2014 | 難しいタスクを生理信号から推定する。 |
| Müller and Fritz 2015 | Stuck/frustrated と progress を分けて扱う。 |
| ScreenAI 2024 / SeeClick 2024 | 画面上のエラー、UI、作業対象を読む。 |
| Brown et al. 2023 | focused work 中かどうかを操作ログから見る。 |

### 4.3 入力特徴量

| feature | 意味 |
| --- | --- |
| `workload_score` | EEG/生理信号由来の負荷 |
| `progress_score` | 成果物変化 |
| `screen_error_flag` | エラー表示 |
| `screen_error_repetition` | 同じエラー/同じ画面の反復 |
| `search_doc_loop_count` | エラー画面とドキュメント検索の往復 |
| `idle_seconds` | 入力停止 |
| `cursor_repetition_score` | 同じ箇所の往復、選択、取り消し |
| `self_report_frustration` | 苛立ち自己報告 |

### 4.4 最初の算出方法

```text
p_stuck =
  sigmoid(
    + 1.5 * workload_score
    - 1.2 * progress_score
    + 1.0 * screen_error_repetition
    + 0.8 * search_doc_loop_count
    + 0.6 * cursor_repetition_score
    + 0.5 * self_report_frustration
  )
```

より単純には、次でもよい。

```text
stuck_score =
  workload_score
  * (1 - progress_score)
  * (1 + screen_error_repetition)
```

### 4.5 評価

- 人手で「詰まっている」とラベルされた区間との一致
- 介入後に再開率や進捗が上がるか
- `高負荷だが進捗あり` との混同行列を見る

## 5. Expert 4: 低活動だが思考中

### 5.1 解く問題

キー入力やマウス入力は少ないが、ユーザが作業対象について考えている状態を検出する。NEDOで非常に重要な状態である。操作ログだけなら「非作業」に見えるが、EEG/視線/画面文脈を足すことで「思考中」と判定できる。

### 5.2 使う先行研究

| 研究 | 借りる部分 |
| --- | --- |
| Kevic et al. 2015 | 操作していないコード要素への視線が、作業注意を表す。 |
| Fritz et al. 2014 | 生理信号が内的難易度/負荷を持つ。 |
| Hamed et al. 2026 | on-screen と on-task を分ける。 |
| Medeiros et al. 2024 | EEGを実作業認知状態の参照信号として扱う。 |

### 5.3 入力特徴量

| feature | 意味 |
| --- | --- |
| `idle_seconds` | 入力停止時間 |
| `workload_score` | EEG/EDA/瞳孔の負荷 |
| `attention_score` | 視線、画面、作業関連度からの注意 |
| `screen_todo_related_score` | 画面が現在Todoと関連する度合い |
| `gaze_on_task_score` | 作業対象への視線 |
| `app_switch_count` | 切替少なさ |
| `screen_text_reading_score` | 文書/コード読解らしさ |

### 5.4 最初の算出方法

```text
p_thinking =
  sigmoid(
    + 1.3 * idle_score
    + 1.2 * workload_score
    + 1.0 * attention_score
    + 1.0 * screen_todo_related_score
    - 1.2 * context_switch_score
    - 1.0 * distracted_score
  )
```

視線がない初期実装では、`screen_todo_related_score` と `active_app`、`screen_text_reading_score` で近似する。

### 5.5 評価

- 作業後リプレイで「この時間は考えていた」とラベルされた区間との一致
- `離脱・マインドワンダリング` との混同率
- 入力停止をすべて非作業扱いするベースラインより改善するか

## 6. Expert 5: 離脱・マインドワンダリング

### 6.1 解く問題

作業から注意が外れている状態を検出する。これは、入力停止だけでは判定できない。低活動だが思考中との弁別が重要である。

### 6.2 使う先行研究

| 研究 | 借りる部分 |
| --- | --- |
| Hamed et al. 2026 | on-screen/on-task を分け、マインドワンダリングを検出する発想。 |
| Altuwairqi et al. 2021 | マウス/キーボード/顔から engagement を推定する。 |
| Xue et al. 2024/2025 | EEG・視線・顔を使ったオンライン学習負荷/関与推定。 |
| Brown et al. 2023 | focused work 候補区間から外れる時間を行動ログで扱う。 |

### 6.3 入力特徴量

| feature | 意味 |
| --- | --- |
| `idle_seconds` | 入力停止 |
| `workload_score` | 低負荷 |
| `attention_score` | 低注意 |
| `screen_todo_related_score` | 画面がTodoと関係ない |
| `unrelated_app_seconds` | 作業外アプリ |
| `gaze_off_screen_score` | 画面外視線 |
| `face_engagement_score` | 顔/姿勢からのengagement |

### 6.4 最初の算出方法

```text
p_distracted =
  sigmoid(
    + 1.0 * idle_score
    + 1.2 * unrelated_app_score
    + 1.0 * gaze_off_screen_score
    - 1.2 * workload_score
    - 1.0 * screen_todo_related_score
    - 0.8 * progress_score
  )
```

視線・顔がない場合は、作業外アプリ時間、Todo非関連画面、低負荷、低進捗で近似する。

### 6.5 評価

- 作業後リプレイでの mind wandering / off-task ラベル
- `thinking` との弁別
- 休憩提案やリマインドの納得度

## 7. Expert 6: 中断・タスク切替

### 7.1 解く問題

通知、アプリ切替、別Todo、チャット、ブラウザ検索などにより、作業文脈が切り替わった状態を検出する。

これは比較的、操作ログ中心で扱える。EEGを使わなくてもよい可能性が高い。

### 7.2 使う先行研究

| 研究 | 借りる部分 |
| --- | --- |
| Brown et al. 2023 | ログから関連行動の連続性/中断を扱う。 |
| Kevic et al. 2015 | IDE内ナビゲーションや操作ログで作業対象遷移を見る。 |
| ScreenAI 2024 / SeeClick 2024 | 画面やUIから現在の作業対象を推定する。 |

### 7.3 入力特徴量

| feature | 意味 |
| --- | --- |
| `app_switch_count` | アプリ切替回数 |
| `active_app_entropy` | 使用アプリの散らばり |
| `todo_related_score_delta` | Todo関連度の急落 |
| `screen_embedding_distance` | 画面文脈の急変 |
| `notification_event_count` | 通知/チャット |
| `browser_tab_switch_count` | タブ切替 |
| `task_id_change` | 作業対象Todoの変化 |

### 7.4 最初の算出方法

```text
p_switching =
  sigmoid(
    + 1.3 * app_switch_count_norm
    + 1.2 * active_app_entropy
    + 1.0 * screen_embedding_distance
    + 1.0 * notification_event_count
    + 0.8 * browser_tab_switch_count
    - 1.0 * related_action_session_score
  )
```

これは、最初からほぼルールベースで実装可能である。

### 7.5 評価

- 人手で見たタスク切替区間との一致
- Todoとの関連度が急落した区間との一致
- focused work metric の分断点と一致するか

## 8. 最終ラベル出力層

### 8.1 単純な argmax

最初は、6つの expert 確率の最大値でラベルを決める。

```text
state(t) = argmax_k p_k(t)
```

ただし、状態には優先順位がある。例えば `switching` は、短時間でも明示的なアプリ/タスク切替があれば優先してよい。`stuck` は、`highload_work` より介入対象として優先されることがある。

### 8.2 重み付き統合

次に、状態ごとの重みを導入する。

```text
logit_state(t) = W p(t) + b
state(t) = softmax(logit_state(t))
```

ここで `p(t)` は expert 出力である。

```text
p(t) = [
  p_focused,
  p_highload_work,
  p_stuck,
  p_thinking,
  p_distracted,
  p_switching
]
```

`W` は最初は手で設定し、ラベルが集まったら学習する。

### 8.3 状態遷移を入れる

作業状態は時間的に連続するため、HMMやCRF風に遷移確率を入れると安定する。

```text
score(state_t = k) =
  emission_score_k(t)
  + transition_score(prev_state, k)
```

例:

- `focused -> focused` は起こりやすい
- `focused -> switching` は通知やアプリ切替があると起こる
- `thinking -> stuck` は長時間進捗がないと起こる
- `stuck -> focused` はタスク細分化や解決後に起こる

最初は移動平均やヒステリシスでもよい。

```text
state changes only if new state remains top for N consecutive windows
```

## 9. 先行研究との対応表

| Expert | 主なモーダル | 借りるモデル/指標 | 先行研究 |
| --- | --- | --- | --- |
| focused / flow-like | 操作ログ、進捗、自己報告 | focus time, related action session, diary validation | Brown et al. 2023 |
| highload_work | EEG/EDA/ECG/瞳孔、進捗 | workload classifier + progress score | Fritz et al. 2014, CLARE 2024, CL-Drive 2024 |
| stuck | EEG/EDA、進捗、画面エラー、操作反復 | difficulty classifier + low progress + error loop | Fritz et al. 2014, Müller and Fritz 2015, ScreenAI 2024 |
| thinking | 入力停止、EEG/注意、作業画面 | idle + workload/attention + on-task screen | Kevic et al. 2015, Hamed et al. 2026, Medeiros et al. 2024 |
| distracted | 入力停止、作業外画面、低負荷、視線/顔 | off-task/on-screen distinction, engagement score | Hamed et al. 2026, Altuwairqi et al. 2021, Xue et al. 2024/2025 |
| switching | アプリ/画面/Todo遷移 | app switch, context distance, interruption events | Brown et al. 2023, Kevic et al. 2015, ScreenAI/SeeClick 2024 |

## 10. 状態 x モーダル対応表

この表は、6状態を推定するときに、どのモーダルがどの先行研究に支えられているかを示す。空欄は「使えない」という意味ではなく、その状態の主要根拠としては優先度が低い、または追加調査が必要という意味である。

| 状態 | EEG/生理信号 | 操作ログ | 画面録画/OCR/VLM | 視線/顔 | 成果物/進捗 | 自己報告 |
| --- | --- | --- | --- | --- | --- | --- |
| 順調な集中・flow-like | Müller and Fritz 2015: 感情/進捗の補助。Girardi et al. 2020: 開発中感情。 | Brown et al. 2023: focus time / related action session。 | ScreenAI 2024: 作業画面の文脈確認。 | Kevic et al. 2015: 操作されない対象への注意補助。 | Brown et al. 2023, Müller and Fritz 2015: 進捗軸。 | Brown et al. 2023: diary validation。flow-like の補助ラベル。 |
| 高負荷だが進捗あり | Fritz et al. 2014: task difficulty。CLARE 2024, CL-Drive 2024: workload classifier。Xue et al. 2024/2025: EEG/視線/顔の負荷評価。 | Brown et al. 2023: focused work 内の活動継続。 | ScreenAI 2024: 画面上の作業文脈。 | Fritz et al. 2014: eye tracking。CLARE/CL-Drive: gaze。 | Müller and Fritz 2015: high/low progress。git差分/テスト成功で近似。 | CLARE/CL-Drive: 10秒負荷自己報告。Müller and Fritz 2015: 進捗自己評価。 |
| 高負荷で停滞 | Fritz et al. 2014: difficulty。CLARE 2024: workload。Müller and Fritz 2015: stuck/frustrated 系の生体信号。 | Brown et al. 2023: focused work から外れないが進まない区間。操作反復。 | ScreenAI 2024 / SeeClick 2024: エラー表示、同一画面反復、UI文脈。 | Fritz et al. 2014: 視線特徴。Kevic et al. 2015: 同一対象への注視。 | Müller and Fritz 2015: low progress。ビルド/テスト失敗、差分少。 | Müller and Fritz 2015: frustration/progress自己評価。 |
| 低活動だが思考中 | Fritz et al. 2014: 生理信号で難しさ推定。Medeiros et al. 2024: EEGを認知状態参照信号として扱う。 | 入力停止/低操作量。ただし単独では離脱と混同。 | ScreenAI 2024: 作業対象画面が維持されているか。 | Kevic et al. 2015: 操作していないコード要素への視線。Hamed et al. 2026: on-task/on-screen 分離。 | 進捗は短期的には低いことが多い。長い窓で後続進捗を見る。 | 作業後リプレイで「考えていた」ラベルを取得。CLARE/CL-Driveの短周期自己報告は参考。 |
| 離脱・マインドワンダリング | 低負荷/低覚醒の補助。Xue et al. 2024/2025: EEG/視線/顔の関与推定。 | Brown et al. 2023: focus time から外れる区間。低操作/無関係操作。 | Hamed et al. 2026: 画面を見ていても内容を考えていない可能性。VLMで作業外画面確認。 | Hamed et al. 2026: on-screen/on-task。Altuwairqi et al. 2021: 顔/マウス/キーボード engagement。 | 進捗低下、成果物変化なし。 | off-task / mind wandering の自己報告。 |
| 中断・タスク切替 | 生理信号は主根拠ではなく、切替後負荷変化の補助。 | Brown et al. 2023: 関連行動の分断。アプリ/ツール切替。Kevic et al. 2015: IDE内ナビゲーション。 | ScreenAI 2024 / SeeClick 2024: 画面文脈、UI、作業対象の急変。 | 視線は補助。タスク外対象への移動確認。 | Todo/成果物対象の変化。git差分の対象変更。 | 中断理由、意図的切替か外的割り込みかの確認。 |

### 10.1 表から見える設計方針

この表から、状態ごとに中心モーダルが異なることがわかる。

- `focused / flow-like` は、操作ログと進捗、自己報告が中心で、EEGは補助でよい。
- `highload_work` と `stuck` は、EEG/生理信号と進捗の組み合わせが中心になる。
- `thinking` と `distracted` は、どちらも低活動に見えるため、EEG/視線/画面文脈で弁別する。
- `switching` は、操作ログと画面文脈だけでもかなり検出でき、EEGは主役ではない。

したがって、NEDOシステムの設計では、すべての状態に全モーダルを均等に使う必要はない。各状態に対して、先行研究で妥当性が示されたモーダルと軽量な算出方法を割り当て、最後に expert 出力を統合するのがよい。

## 11. 実装優先度

| 優先度 | Expert | 理由 |
| --- | --- | --- |
| 1 | `stuck` | 高負荷停滞はタスク細分化エージェントの主要介入対象。EEG/進捗/画面エラーで比較的定義しやすい。 |
| 2 | `thinking` | 操作ログだけでは非作業扱いされる区間を救えるため、EEGを使う意義が大きい。 |
| 3 | `switching` | 操作ログと画面文脈で実装しやすく、作業レポートの要因説明に直結する。 |
| 4 | `highload_work` | stuck との弁別に必要。進捗指標が整ってから精度が上がる。 |
| 5 | `focused / flow-like` | focused work は可能だが、flow-like と呼ぶには自己報告が必要。 |
| 6 | `distracted` | thinking との弁別に視線/顔/自己報告がほしいため、後段でよい。 |

## 12. この設計の強み

### 12.1 先行研究を部品として説明できる

各論文が何を解いたのかが、状態 expert と対応する。これにより、NEDO提案では「最近の研究を大きなモデルに混ぜる」ではなく、「既存研究が個別に解いてきた小問題を、作業レポート生成に向けて統合する」と説明できる。

### 12.2 機械学習なしでも初期実装できる

最初は各 expert をルールベースやスコア関数で作れる。

```text
p_stuck = workload_score * (1 - progress_score) * error_loop_score
p_switching = app_switch_score + screen_context_distance
p_thinking = idle_score * workload_score * todo_related_score
```

これは実装しやすく、かつ後から機械学習モデルに置き換えやすい。

### 12.3 解釈可能性が高い

各 expert がどのモーダルを見て判定したかを説明できる。これは、作業レポートの納得度に直結する。

### 12.4 評価しやすい

状態ごとに評価できる。

- stuck expert の評価: stuckラベルとの一致、介入後改善
- thinking expert の評価: 入力停止を非作業扱いするベースラインとの比較
- switching expert の評価: 人手タスク切替ラベルとの一致

大きなブラックボックスモデルより、どこが弱いかを診断しやすい。

## 13. 注意点

### 13.1 確率は真の確率ではなく、最初はスコアでよい

初期実装の `p_stuck` や `p_thinking` は、厳密な確率ではなく 0-1 の状態らしさスコアでよい。ラベルデータが増えたら Platt scaling や isotonic regression で calibration する。

### 13.2 状態は排他的とは限らない

`highload_work` と `focused` は同時に高くなりうる。`thinking` と `stuck` も近い。したがって、最終ラベルは1つにしても、レポートでは上位2状態を出す方がよい。

```json
{
  "primary_state": "stuck",
  "secondary_state": "thinking",
  "state_probs": {
    "stuck": 0.72,
    "thinking": 0.61
  }
}
```

### 13.3 flow は proxy として扱う

`flow_like` は、心理学的flowそのものではなく、focused work + progress + low interruption + positive self-report の proxy である。これは Brown et al. 2023 の限界認識と整合する。

### 13.4 C(t) は分類器ではなく説明器に近い

画面文脈 `C(t)` は、状態を直接分類するというより、状態判定の根拠を説明する役割が大きい。ScreenAI/SeeClick/VLM は、`stuck` や `switching` の原因候補を抽出するモジュールとして使う。

## 14. Next Actions

- `nedo/drafts/2026-06-05_system_problem_decomposition.md` に、この6 expert model の方針を反映する。
- 各 expert について、必要特徴量を `features.md` あるいはデータスキーマ案として分離する。
- 先行研究ごとに、どの expert のどの特徴量/分類器に対応するかを個別要約へ分割する。
- 最初の実装案では、`stuck`, `thinking`, `switching` の3 expert から始めるとよい。これらはNEDOの価値に直結し、ルールベースで開始しやすい。
