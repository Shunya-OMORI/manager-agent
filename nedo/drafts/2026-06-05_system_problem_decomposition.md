# NEDO 集中力・認知負荷変化の定義問題とシステム分解

## Summary

この文書の責務は、NEDO システムを単なる機能一覧として分解することではない。中心課題は、最終的にシステムが出力する「集中力や認知負荷の変化を踏まえた作業レポート」において、集中力・認知負荷・フロー・停滞・離脱をどのように学術的に定義し、その定義が良いものだとどのように評価するかを整理することである。

結論は、集中力変化を EEG の単一指標、例えば `beta / (alpha + theta)` の閾値超過として定義するのは弱い、ということである。EEG は内的状態を観測するが、作業文脈、操作量、作業速度、成果物変化、エラー、画面上の詰まりの原因を直接は説明しない。一方、画面・操作ログは作業行動と成果に近い情報を持つが、手が止まっている区間が深い思考なのか、迷いなのか、離脱なのかを単独では弁別しにくい。

したがって、本システムで採用すべき定義は、単一モダリティの指標ではなく、多モーダル観測から推定される潜在状態としての定義である。数学的には、EEG/生理信号、画面録画、操作ログ、成果物変化、自己報告を観測変数とし、集中・認知負荷・フロー・停滞・離脱を潜在変数として推定する問題に分解するのが筋がよい。

ただし、これは実装不能な概念問題ではない。最初の実装では、潜在状態 `Z(t)` を「時間窓ごとの特徴量ベクトルから計算される数個のスコア」として扱えばよい。つまり、古典的機械学習や深層学習で自然に扱える、行列 `X`、ラベル `y`、スコア `s`、分類器 `f` の問題へ落とせる。

```text
X = [x_1, x_2, ..., x_T]^T
x_t = [eeg_features, action_features, screen_features, progress_features]

z_t = f_score(x_t)
y_t = f_label(z_t)
change_t = g(z_t, z_{t-1})
```

ここで `x_t` は 10秒、30秒、60秒などの時間窓から作る特徴量ベクトルである。`z_t` は認知負荷、活動量、進捗、文脈切替などのスコアベクトルであり、`y_t` は「順調」「高負荷停滞」「思考中」「離脱」などの状態ラベルである。最初から高度な潜在変数モデルを作る必要はない。

この実装方針をさらに具体化するには、全モーダルを1つの巨大モデルに投入するのではなく、6つの状態ごとに小さな expert model を置くのがよい。詳細は `nedo/drafts/2026-06-05_statewise_expert_model_design.md` に整理した。

```text
p_focused(t)       = expert_focused(x_t)
p_highload_work(t) = expert_highload_work(x_t)
p_stuck(t)         = expert_stuck(x_t)
p_thinking(t)      = expert_thinking(x_t)
p_distracted(t)    = expert_distracted(x_t)
p_switching(t)     = expert_switching(x_t)

state(t) = output_layer([p_focused, p_highload_work, p_stuck, p_thinking, p_distracted, p_switching])
```

この構成にすると、Brown et al. 2023 の focused work metric、Fritz et al. 2014 や CLARE/CL-Drive の負荷推定、Müller and Fritz 2015 の進捗/感情分類、Kevic et al. 2015 の視線・操作ログ統合、ScreenAI/SeeClick の画面文脈理解を、それぞれ別の小モデルとして組み合わせられる。

## 0. 実装に落とした最小モデル

最初のプロトタイプでは、問題を次のように定義する。

```text
入力:
  時間窓ごとの EEG 特徴量
  時間窓ごとのキー/マウス/アプリ操作ログ
  時間窓ごとの画面OCR/VLM要約
  時間窓ごとの成果物変化

出力:
  workload_score      : 0.0 - 1.0
  activity_score      : 0.0 - 1.0
  progress_score      : 0.0 - 1.0
  context_switch_score: 0.0 - 1.0
  stuck_score         : 0.0 - 1.0
  state_label         : one of {focused, thinking, stuck, flow_like, distracted, switching}
  report_evidence     : どの特徴量によりその判定になったか
```

この形なら、実装はかなり素直である。最初は scikit-learn のロジスティック回帰、Random Forest、XGBoost/LightGBM、あるいは時系列を少し見るなら HMM や Temporal CNN に落とせる。深層学習を使わなくても、特徴量設計とラベル設計ができれば開始できる。

### 0.1 時間窓ごとの特徴量テーブル

最初に作るべき中心データ構造は、次のような `pandas.DataFrame` である。

| column | 型 | 意味 |
| --- | --- | --- |
| `window_start` | datetime | 時間窓の開始 |
| `window_end` | datetime | 時間窓の終了 |
| `eeg_alpha_mean` | float | alpha帯域平均 |
| `eeg_beta_mean` | float | beta帯域平均 |
| `eeg_theta_mean` | float | theta帯域平均 |
| `eeg_beta_alpha_theta_ratio` | float | `beta / (alpha + theta)` |
| `eeg_workload_model_score` | float | EEGモデルからの負荷スコア |
| `key_count` | int | キー入力数 |
| `mouse_count` | int | マウス操作数 |
| `idle_seconds` | float | 入力がなかった秒数 |
| `app_switch_count` | int | アプリ切替回数 |
| `active_app` | string | 主なアプリ |
| `screen_text_len` | int | OCRテキスト量 |
| `screen_error_flag` | bool | エラー表示の有無 |
| `screen_task_embedding_*` | float | 画面要約の埋め込み |
| `git_lines_changed` | int | 変更行数 |
| `test_fail_count` | int | テスト失敗数 |
| `todo_related_flag` | bool | Todoと画面内容が関連するか |
| `self_report_workload` | int/null | 作業後または中断時の負荷ラベル |
| `self_report_focus` | int/null | 作業後または中断時の集中ラベル |
| `human_label` | string/null | 人手で付けた状態ラベル |

このテーブルができれば、以降は通常の機械学習問題になる。

```text
X = df[feature_columns].values
y = df["human_label"].values
model.fit(X, y)
```

### 0.2 実装しやすい状態ラベル

最初から「集中力」「フロー」を直接ラベルにしない方がよい。曖昧だからである。まずは、観測から比較的ラベル付けしやすい状態へ落とす。

| ラベル | 定義 | 典型的な特徴量パターン |
| --- | --- | --- |
| `focused` | 作業に向かい、進捗もある | activity高、progress高、switch低、workload中 |
| `thinking` | 入力は少ないが作業文脈に留まり、内的負荷がある | idle高、workload中-高、screenが作業関連 |
| `stuck` | 負荷が高いが進捗が低い | workload高、progress低、error反復、同画面滞在 |
| `flow_like` | 進捗が高く、切替が少なく、負荷が過剰でない | progress高、activity安定、switch低、self_report良 |
| `distracted` | 作業から注意が外れる | idle高、workload低、screen/active_appが作業外 |
| `switching` | タスク・アプリ・文脈が頻繁に切り替わる | app_switch高、todo関連低、短時間画面遷移 |

ここでの `flow_like` は、心理学的な flow を完全に測るという意味ではない。操作ログ・進捗・自己報告から近似される「フローらしい作業区間」である。これにより、Brown et al. 2023 が指摘する「ログだけではflowそのものは難しい」という限界を避けられる。

### 0.3 スコア計算から始めるルールベース版

教師データが少ない最初期は、分類器ではなくルールベースでよい。

```text
workload_score =
  normalize(eeg_workload_model_score)

activity_score =
  normalize(key_count + mouse_count)

progress_score =
  normalize(git_lines_changed + task_completion_events - test_fail_count)

context_switch_score =
  normalize(app_switch_count + unrelated_app_seconds)

stuck_score =
  workload_score * (1 - progress_score) * (1 + screen_error_flag)
```

状態ラベルも、最初は if 文で十分である。

```text
if stuck_score > 0.7:
    state = "stuck"
elif idle_seconds > threshold and workload_score > 0.5 and todo_related_flag:
    state = "thinking"
elif progress_score > 0.7 and context_switch_score < 0.3:
    state = "focused"
elif context_switch_score > 0.7:
    state = "switching"
else:
    state = "unknown"
```

このルールベース版は、論文的にはベースラインになる。後から Random Forest や LightGBM と比較すれば、「単純な閾値より多モーダル学習の方がよい」と評価できる。

### 0.4 機械学習版

人手ラベルまたは自己報告ラベルが増えたら、次のように教師あり分類へ移る。

```text
X_t = [
  eeg_alpha_mean,
  eeg_beta_mean,
  eeg_theta_mean,
  eeg_workload_model_score,
  key_count,
  mouse_count,
  idle_seconds,
  app_switch_count,
  screen_error_flag,
  screen_task_embedding,
  git_lines_changed,
  test_fail_count,
  todo_related_flag
]

y_t = human_label
```

モデル候補:

| モデル | 使いどころ |
| --- | --- |
| Logistic Regression | まず説明しやすいベースライン |
| Random Forest | 非線形・特徴量重要度を見たい |
| LightGBM/XGBoost | 表形式特徴量で強い |
| HMM | 状態遷移を明示的に扱いたい |
| Temporal CNN / LSTM | 時系列窓の連続性を深層学習で扱いたい |

実装初期では LightGBM または Random Forest が現実的である。EEGの前処理は MNE、特徴量テーブルは pandas、分類は scikit-learn 系で組むと、人間が読みやすい。

### 0.5 変化検出

状態ラベルが出た後、集中力変化は単純にスコア差分で検出できる。

```text
z_t = [
  workload_score,
  activity_score,
  progress_score,
  context_switch_score,
  stuck_score
]

change_score_t = norm(z_t - z_{t-1})
change_t = change_score_t > tau
```

または、状態ラベルの遷移として検出する。

```text
change_t = state_t != state_{t-1}
```

最初はこの程度で十分である。後から `ruptures` などの変化点検出ライブラリを使えば、時系列全体から変化区間を検出できる。

### 0.6 レポート生成に渡すJSON

最終的にエージェントへ渡すデータは、次の JSON にすればよい。

```json
{
  "window_start": "2026-06-05T13:20:00",
  "window_end": "2026-06-05T13:21:00",
  "state": "stuck",
  "scores": {
    "workload": 0.82,
    "activity": 0.31,
    "progress": 0.12,
    "context_switch": 0.18,
    "stuck": 0.88
  },
  "evidence": {
    "eeg": "workload_score increased",
    "actions": "low input and repeated cursor movement",
    "screen": "same error message remained visible",
    "progress": "no file diff in this window"
  },
  "suggested_intervention": "break current task into smaller debugging steps"
}
```

つまり、システムの実装責務はかなり明確になる。

1. センサ・ログを時間窓にそろえる。
2. 各窓から特徴量を作る。
3. スコアを計算する。
4. 状態ラベルを出す。
5. 変化点を検出する。
6. 根拠と画面文脈をJSONにまとめる。
7. LLMがレポートとTodo更新案を書く。

## 1. 何を定義しなければならないか

### 1.1 定義対象

NEDO システムが定義すべき対象は、単なる「集中力スコア」ではなく、作業レポートと Todo 更新に使える作業状態である。少なくとも次の状態を区別できる必要がある。

| 状態 | 直感的な意味 | なぜ区別が必要か |
| --- | --- | --- |
| 順調な集中 | 作業が進み、内的負荷も過度ではない | 介入せず維持するべき状態 |
| フロー | 高い没入、肯定的感情、進捗感がある | 割り込みを避けるべき状態 |
| 高負荷だが進捗あり | 難しいが前に進んでいる | 支援は控えめでよい |
| 高負荷で停滞 | 負荷が高く、操作や成果が進まない | タスク細分化やヒントが有効 |
| 低活動だが思考中 | 入力は止まるが、内的処理は続いている | 非作業と誤判定してはいけない |
| 離脱・マインドワンダリング | 作業から注意が外れている | 休憩やリマインドの対象 |
| 中断・文脈切替 | 通知、別アプリ、別タスクへ移った | 生産性低下要因として記録すべき |

この分類は、既存研究の整理と整合する。Brown et al. 2023 は操作ログから focused work を推定できる一方、flow そのものはログだけでは切り分けにくいことを示した。Müller and Fritz 2015 は感情と進捗を別軸として扱い、Fritz et al. 2014 は生理信号から課題難易度を推定した。Kevic et al. 2015 は操作ログと視線が異なる情報を持つことを示した。これらを合わせると、「集中力変化」を単一軸でなく、内的負荷・注意・進捗・情動・作業文脈の組み合わせとして扱う方が自然である。

### 1.2 定義の失敗例

弱い定義は、次のような反例で破綻する。

| 定義案 | 反例 | 破綻する理由 |
| --- | --- | --- |
| EEG の特定周波数比が閾値を超えたら高集中 | 難問に詰まり、負荷だけが上がっている | 高集中と高負荷停滞を区別できない |
| キー入力・マウス入力が多ければ集中 | 急いで雑に作業している、またはエラー対応に追われている | 作業品質や内的負荷を見ていない |
| 入力が止まったら集中低下 | 読解・設計・熟考中 | 手の停止と思考停止を混同する |
| 画面が作業アプリなら on-task | 画面を見ながら別のことを考えている | on-screen と on-task を混同する |
| 自己報告だけで集中を決める | 回顧バイアス、報告負荷、作業中断 | 連続的な変化検出に使いにくい |

よい定義は、これらの反例に耐えなければならない。したがって、定義問題は「ある指標を選ぶ問題」ではなく、「反例を区別できる観測設計と推定モデルを作る問題」である。

## 2. 数学的な問題設定

### 2.1 観測変数

作業時間を離散時刻 `t = 1, ..., T` に分ける。各時刻または時間窓に対して、次の観測を置く。

| 記号 | 意味 | 例 |
| --- | --- | --- |
| `X_eeg(t)` | EEG/生理信号 | 周波数帯域、接続性、Hjorth 特徴、EDA、ECG、瞳孔 |
| `X_act(t)` | 操作ログ | キー入力、マウス、アプリ遷移、IDE操作、git差分 |
| `X_scr(t)` | 画面文脈 | 画面録画、OCR、UI要素、エラー表示、文書内容 |
| `X_perf(t)` | 成果・進捗 | 編集量、ビルド結果、テスト結果、完成物の変化 |
| `Y_self(t)` | 自己報告 | NASA-TLX、flow、疲労、集中、負荷の短い報告 |
| `E(t)` | 外部イベント | 通知、割り込み、環境変化、時刻、タスク切替 |

ここで重要なのは、`X_eeg` と `X_act` と `X_scr` が同じものを測っていないことである。EEG は内的状態、操作ログは行動、画面は文脈、成果物は結果を表す。これらは冗長なデータではなく、潜在状態の異なる側面を観測している。

### 2.2 潜在状態

システムが推定したい潜在状態を `Z(t)` と置く。`Z(t)` は単一ラベルでもよいが、NEDO では多次元状態として扱う方がよい。

```text
Z(t) = [W(t), A(t), F(t), P(t), V(t), C(t)]
```

| 成分 | 意味 | 主な根拠モダリティ |
| --- | --- | --- |
| `W(t)` | mental workload / 認知負荷 | EEG、EDA、ECG、瞳孔、自己報告 |
| `A(t)` | attention / on-taskness | 視線、画面、操作ログ、自己報告 |
| `F(t)` | flow / 没入・肯定的集中 | 自己報告、感情、生理信号、進捗 |
| `P(t)` | progress / 作業進捗 | 操作ログ、成果物、画面文脈 |
| `V(t)` | valence / 快不快・苛立ち | 生理信号、顔、自己報告 |
| `C(t)` | context / 作業文脈・要因 | 画面録画、OCR、VLM、git差分 |

集中力変化は、この潜在状態の変化として定義する。

```text
change(t) = 1  if  D(Z(t), Z(t - delta)) > tau
```

ここで `D` は状態間距離、`delta` は比較窓、`tau` は変化点閾値である。ただし、`Z(t)` は直接観測できないため、実際には多モーダル観測から事後分布を推定する。

```text
p(Z(t) | X_eeg(1:t), X_act(1:t), X_scr(1:t), X_perf(1:t), Y_self(1:t), E(1:t))
```

この式が、NEDO システムの学術的な中心である。

### 2.3 なぜ多モーダルでなければならないか

もし各モダリティが潜在状態 `Z` について相補的な情報を持つなら、情報理論的に、多モーダル観測を使う方が単一モダリティより不確実性を減らせる。

```text
H(Z | X_eeg, X_act, X_scr) <= H(Z | X_eeg)
H(Z | X_eeg, X_act, X_scr) <= H(Z | X_act)
H(Z | X_eeg, X_act, X_scr) <= H(Z | X_scr)
```

等号になるのは、追加したモダリティが既存モダリティに対して新しい情報を持たない場合だけである。しかし、先行研究はその逆を示している。

- Brown et al. 2023: 操作ログは focused work 候補を作れるが、flow の主観的側面は残る。
- Kevic et al. 2015: 視線は操作ログと異なるコード注意情報を持つ。
- Fritz et al. 2014: 生理信号は作業難易度を推定する情報を持つ。
- Müller and Fritz 2015: 感情と進捗は別軸として推定できる。
- CLARE/CL-Drive: 評価条件によって有効なモダリティ組み合わせが変わる。

したがって、NEDO の定義は「EEG が正しい」「操作ログが正しい」という単独正解ではなく、各モダリティが `Z(t)` の異なる成分を制約する推定問題として構成するのが妥当である。

## 3. 定義方法のバリエーション

### Definition A: EEG閾値定義

```text
score(t) = beta(t) / (alpha(t) + theta(t))
change(t) = 1 if score(t) > tau
```

最も単純な定義である。実装しやすく、説明もしやすい。しかし、タスク依存性、個人差、アーティファクト、状態の多義性に弱い。Khan et al. 2025 のレビューが示すように、EEG/視線指標はタスクによって増減が混在するため、単一閾値を一般的な集中力定義として置くのは危険である。

この定義は、NEDO の最終定義ではなく、ベースラインとして扱うべきである。

### Definition B: 生理信号による認知負荷スコア定義

```text
W_hat(t) = f_eegphys(X_eeg(t), EDA(t), ECG(t), pupil(t))
change(t) = 1 if |W_hat(t) - W_hat(t - delta)| > tau
```

Fritz et al. 2014、CLARE 2024、CL-Drive 2024、Xue et al. 2024/2025 に近い定義である。認知負荷を連続またはカテゴリとして推定し、その変化を検出する。

この定義は、内的負荷の推定には強い。一方で、作業が進んでいるか、何に詰まっているか、画面上で何が起きたかを説明するには不足する。

### Definition C: 操作ログによる focused work 区間定義

```text
Fwork_hat(t) = f_act(X_act(t), app_sequence(t), edit_build_doc_cycle(t))
```

Brown et al. 2023 に近い定義である。IDE編集、文書閲覧、ビルド、レビューなどの連続的・関連的な行動から focused work 候補区間を抽出する。

この定義は、ナレッジワーカーの実作業に近く、非侵襲的に使いやすい。しかし、flow と focused work を区別できず、手が止まっている熟考を見落とす可能性がある。

### Definition D: 画面・操作・生理の教師あり分類定義

```text
Z_hat(t) = f_multi(X_eeg(t), X_act(t), X_scr(t), X_perf(t))
```

Altuwairqi et al. 2021、Guntz et al. 2017、Xue et al. 2024/2025 のように、複数モダリティを特徴量として、集中・負荷・エンゲージメント等のラベルを分類する定義である。

この定義は、単一モダリティより性能が高くなる可能性がある。ただし、ラベル設計に依存し、なぜその状態になったかの説明が弱くなる危険がある。

### Definition E: 多モーダル潜在状態定義

```text
p(Z(t) | X_eeg, X_act, X_scr, X_perf, Y_self, E)
```

NEDO の本命となる定義である。集中・負荷・フローを単一スコアではなく、潜在状態 `Z(t)` として推定する。状態変化は `Z(t)` の変化として扱い、レポートでは `C(t)`、つまり画面文脈と外部イベントを用いて要因を説明する。

この定義の強みは、以下の反例を自然に分けられることである。

| 観測 | 解釈候補 | 必要なモダリティ |
| --- | --- | --- |
| 入力停止 + EEG負荷高 + 画面は設計文書 | 熟考中 | EEG、画面、操作ログ |
| 入力停止 + EEG負荷低 + 視線/画面が作業外 | 離脱 | EEG、視線、画面 |
| 入力多い + エラー画面反復 + EDA上昇 | 高負荷で停滞 | 操作ログ、画面、EDA |
| 入力多い + 成果物進捗 + 快/進捗自己報告 | フローまたは順調な集中 | 操作ログ、成果、自己報告 |
| アプリ切替多い + 通知 + 作業成果少 | 中断・文脈切替 | 操作ログ、外部イベント、成果 |

Definition E は最も難しいが、NEDO システムの価値に最も合う。

## 4. 良い定義の評価基準

定義の良し悪しは、分類精度だけでは決まらない。作業レポートと Todo 更新に使う以上、少なくとも次の評価軸が必要である。

### 4.1 構成概念妥当性

定義が、認知負荷、注意、フロー、進捗、情動、文脈を混同せずに扱っているかを見る。

```text
Z(t) = [W(t), A(t), F(t), P(t), V(t), C(t)]
```

例えば、`W(t)` が高いだけで `F(t)` も高いと決めてはいけない。高負荷は、フローにも停滞にもなりうる。Müller and Fritz 2015 が感情と進捗を分けたように、NEDO でも状態成分を分離して定義する必要がある。

### 4.2 収束的妥当性

推定した状態が、同じ概念を測る別の指標と一致するかを見る。

例:

- `W_hat(t)` が高い区間で、自己報告の負荷も高い。
- `A_hat(t)` が高い区間で、on-task/on-screen ラベルも高い。
- `P_hat(t)` が高い区間で、成果物変化やタスク完了が増える。

数学的には、相関、AUC、F1、平均絶対誤差、順位相関、キャリブレーション誤差で評価できる。

### 4.3 弁別的妥当性

似ているが違う状態を区別できるかを見る。ここが NEDO の肝である。

| 区別すべきペア | 単一指標で難しい理由 | 多モーダルでの弁別 |
| --- | --- | --- |
| 熟考 vs 離脱 | どちらも入力が止まる | EEG/視線/画面文脈 |
| focused work vs flow | どちらも作業が続く | 自己報告、感情、進捗 |
| 高負荷進捗あり vs 高負荷停滞 | どちらも負荷が高い | 成果物変化、エラー反復、操作パターン |
| 集中低下 vs 文脈切替 | どちらも元作業から外れる | 外部イベント、アプリ遷移、Todo文脈 |
| 低負荷順調 vs 低負荷退屈 | 生理負荷が低い | 進捗、感情、自己報告 |

良い定義は、これらのペアを人間の評価に近い形で分ける。

### 4.4 時系列妥当性

集中力や認知負荷は点ではなく変化である。したがって、時系列上の変化点検出として評価する必要がある。

```text
change(t) = 1 if D(Z(t), Z(t - delta)) > tau
```

評価指標:

- change point precision / recall
- 人手アノテーションとの差分時間
- 変化検出の遅延
- 誤検出による不要介入率
- 見逃しによる未支援率

ここで単純な分類精度だけを見ると、長い安定区間で高精度に見えてしまう。NEDOでは、変化点が正しく検出されるかを別指標として見る必要がある。

### 4.5 説明妥当性

レポートを出すシステムでは、状態推定だけでなく「なぜそう判定したか」が必要である。

良い定義は、次の形の説明を出せる。

```text
時刻 t で高負荷停滞と判定した。
根拠:
- EEG/EDA から内的負荷が上昇した。
- 操作ログでは同じファイル/画面への往復が増えた。
- 画面録画ではエラー表示とドキュメント検索が反復した。
- 成果物差分は小さかった。
```

この説明は、単なる分類器ではなく、`Z(t)` の各成分と観測モダリティの対応が明示されているから可能になる。

### 4.6 介入妥当性

NEDO システムは観測だけで終わらない。タスク細分化、レポート、Todo 更新という介入につながる。したがって、定義の評価には「その定義で介入したときにユーザにとってよくなるか」を含める必要がある。

評価例:

- 不要な割り込みが減る。
- 高負荷停滞区間の後に、タスク細分化で再開率が上がる。
- 作業後レポートの納得度が高い。
- Todo 更新がユーザの意図と一致する。
- 翌日の計画精度や作業継続時間が改善する。

ここまで満たして初めて、「集中力変化の定義」がプロダクト価値につながったといえる。

## 5. 問題の再分化

NEDO システム全体は、次の小問題に再分化できる。

| 小問題 | 入力 | 出力 | 代表的な先行研究 | 評価 |
| --- | --- | --- | --- | --- |
| P1. 作業区間の生成 | 操作ログ、アプリ遷移、画面録画 | focused work 候補区間 | Brown et al. 2023 | 自己報告との一致、区間精度 |
| P2. 内的負荷推定 | EEG、EDA、ECG、瞳孔 | `W_hat(t)` | Fritz et al. 2014、CLARE 2024、CL-Drive 2024 | AUC、F1、LOSO、キャリブレーション |
| P3. 注意・画面関与推定 | 視線、画面、操作ログ | on-task/on-screen 状態 | Hamed et al. 2026、Kevic et al. 2015 | on-task ラベル一致、注視/操作の相補性 |
| P4. 進捗・停滞推定 | git差分、編集量、エラー、ビルド/テスト | `P_hat(t)` | Müller and Fritz 2015、Brown et al. 2023 | 進捗自己報告、成果物変化 |
| P5. 情動・快不快推定 | EEG、EDA、顔、自己報告 | `V_hat(t)` | Müller and Fritz 2015、Girardi et al. 2020 | 感情ラベル分類、自己報告一致 |
| P6. 文脈・要因説明 | 画面録画、OCR、VLM、操作履歴 | `C_hat(t)`、原因候補 | ScreenAI 2024、SeeClick 2024 | 人手説明との一致、要因ランキング |
| P7. 潜在状態統合 | P1-P6 の出力 | `Z_hat(t)` | 多モーダル学習、CLARE/CL-Drive | アブレーション、情報利得、弁別妥当性 |
| P8. 変化点検出 | `Z_hat(t)` の時系列 | 変化区間 | 時系列変化点検出 | precision/recall、検出遅延 |
| P9. 作業レポート生成 | `Z_hat(t)`, `C_hat(t)`, Todo | レポート、Todo 更新案 | LLM要約、JumpStarter 2024 | 納得度、再現性、行動改善 |

この表で重要なのは、NEDO の新規性が P2 だけではないことだ。EEGで認知負荷を測る研究は既に多い。画面/UI理解も進んでいる。操作ログで focused work を測る研究もある。NEDO の課題は、それらを P7-P9 で統合し、集中力変化の定義を「作業支援に使える状態」として成立させることにある。

## 6. 統合アプローチの論証

### Claim 1: 単一モダリティ定義は反例に弱い

EEG単独では、内的負荷は推定できても作業文脈と成果を観測できない。操作ログ単独では、作業行動は観測できても手の停止と思考停止を区別できない。画面録画単独では、文脈は観測できても内的負荷を直接は観測できない。

よって、単一モダリティの定義関数 `d_i(X_i)` は、少なくとも一部の状態ペアに対して同じ観測を返す。

```text
d_act(熟考) ≈ d_act(離脱)
d_eeg(高負荷進捗あり) ≈ d_eeg(高負荷停滞)
d_scr(on-screenだが別思考) ≈ d_scr(on-screenで熟考)
```

この場合、状態を識別するには観測が不足している。

### Claim 2: 多モーダル統合は識別可能性を上げる

`X_eeg` が内的負荷、`X_act` が作業行動、`X_scr` が文脈、`X_perf` が成果を制約するなら、複数の状態ペアは統合観測で分離できる。

例:

```text
熟考:
  X_act = 入力停止
  X_eeg = 負荷/注意あり
  X_scr = 作業対象画面

離脱:
  X_act = 入力停止
  X_eeg = 負荷/注意低下
  X_scr = 作業外または視線逸脱
```

操作ログだけなら同じ `入力停止` だが、EEG と画面文脈を足すと分離できる。このように、多モーダル統合は単なる精度改善ではなく、状態定義に必要な識別可能性を提供する。

### Claim 3: 良い定義はレポート可能でなければならない

NEDO のアウトプットはスコアではなく作業レポートである。したがって、定義関数は状態ラベルだけでなく、要因説明を返す必要がある。

```text
definition_output(t) = {
  state: Z_hat(t),
  change: change(t),
  evidence: {eeg, action, screen, performance, self_report},
  explanation: C_hat(t),
  suggested_intervention: intervention(t)
}
```

これは、画面録画/VLM と操作ログを定義に含める理由になる。EEGだけでは「負荷が上がった」は言えても、「なぜ上がったか」「次に何を細分化すべきか」は言えない。

### Claim 4: 最終的な定義は、推定精度より介入価値で評価すべきである

集中力変化の定義がどれだけ美しくても、ユーザに不要な割り込みを生むならプロダクトとしては失敗である。逆に、分類精度が完全でなくても、高負荷停滞区間を早く見つけ、次の Todo を適切に細分化できるなら価値がある。

したがって、最終評価関数は次のように置ける。

```text
J(definition) =
  a * validity_score
  + b * explanation_score
  + c * intervention_gain
  - d * interruption_cost
  - e * privacy_cost
```

ここで `validity_score` は自己報告・成果・人手評価との一致、`explanation_score` はレポートの納得度、`intervention_gain` はTodo更新や再開支援による改善、`interruption_cost` は不要介入、`privacy_cost` は記録範囲と機微情報リスクである。

NEDO で目指すべき良い定義は、この `J` を最大化する定義である。

## 7. NEDOで採用すべき定義

### 推奨定義

> 集中力・認知負荷の変化とは、作業中に観測される EEG/生理信号、画面録画、操作ログ、成果物変化、自己報告を統合して推定される多次元潜在状態 `Z(t)` の時系列変化である。`Z(t)` は少なくとも認知負荷、注意、フロー/没入、進捗、情動、作業文脈から構成され、変化区間は `Z(t)` の状態距離、または状態遷移確率の変化によって検出する。レポートでは、その変化の根拠となった各モダリティと、画面/VLMから推定された作業要因を同時に提示する。

### 最初の実証で使う簡約版

最初から完全な潜在状態モデルを作るのは難しいため、実証では次の簡約版から始める。

```text
Z_simple(t) = [W(t), A(t), P(t), C(t)]
```

| 成分 | 実装上の近似 |
| --- | --- |
| `W(t)` | EEG/EDA/ECG/瞳孔からの負荷スコア |
| `A(t)` | 操作ログ、画面、視線または画面注視の近似 |
| `P(t)` | 編集量、差分、エラー反復、タスク完了 |
| `C(t)` | 画面OCR/VLMによる作業文脈説明 |

これにより、最低限「入力停止だが思考中」「高負荷で停滞」「順調な集中」「中断・文脈切替」を分けられる。

### 最小実験デザイン

1. ナレッジワーカーに近い作業を設定する。例: コーディング、論文要約、設計文書作成。
2. EEG/生理信号、画面録画、操作ログ、成果物差分を同期する。
3. 作業後、区間ごとに自己報告を取る。自然作業中に10秒ごとの報告を求めると負担が大きいため、CLARE/CL-Drive の設計を参考にしつつ、作業後リプレイによるアノテーションも検討する。
4. まず操作ログから focused work 候補区間を作る。
5. その区間を EEG/生理信号と画面文脈で、「順調」「高負荷進捗あり」「高負荷停滞」「思考中」「離脱」に分類する。
6. 人手評価と比較し、弁別的妥当性、説明妥当性、介入妥当性を評価する。

## 8. 提案書に入れるべき筋

提案書では、次の順序で書くと筋が通る。

1. ナレッジワーカーの生産性は、作業時間だけでなく、認知負荷、注意、進捗、感情、作業文脈により左右される。
2. 既存の集中支援ツールは、多くの場合、時間管理やTodo管理に留まり、実際の作業中の認知状態と作業文脈を閉ループで扱わない。
3. EEG/生理信号は内的状態を観測できるが、作業文脈と成果を説明できない。
4. 画面・操作ログは作業文脈と成果を観測できるが、手が止まっている時の内的状態を弁別できない。
5. 先行研究は、操作ログ、視線、EEG/生理信号、画面録画、多モーダル学習の各部分で有効性を示している。
6. しかし、これらを統合して「集中力・認知負荷の変化を、レポートとTodo更新に使える状態」として定義する研究・システムは未成熟である。
7. 本事業は、集中力変化を多モーダル潜在状態の変化として定義し、変化区間の要因を画面/VLMで説明し、Todo更新やタスク細分化へ接続する。

この論理で書けば、「最近の研究が解いた小問題を組み合わせればシステム全体が完成する」というより強い主張になる。つまり、各論文は単なる関連研究ではなく、`Z(t)` の各成分を観測・推定・評価するための部品として位置づく。

## 9. 参照する先行研究の役割

| 研究 | NEDOでの役割 |
| --- | --- |
| Brown et al. 2023 | 操作ログで focused work 候補を作る根拠。ただし flow との弁別限界も示す。 |
| Kevic et al. 2015 | 視線と操作ログが異なる作業注意情報を持つ根拠。 |
| Konopka 2015 | 画面/ナビゲーションが作業対象間の関係を表すデータになりうる根拠。 |
| Fritz et al. 2014 | EEG/視線/EDAでタスク難易度を推定できる根拠。 |
| Müller and Fritz 2015 | 感情と進捗を別軸として扱う根拠。 |
| Guntz et al. 2017 | 画面ベース問題解決で多モーダル統合が単一モダリティを上回る根拠。 |
| Hamed et al. 2026 | on-screen と on-task を分ける必要性の根拠。 |
| Altuwairqi et al. 2021 | 表情・マウス・キーボード統合でエンゲージメント推定が改善する根拠。 |
| Xue et al. 2024/2025 | EEG・視線・顔による多モーダル認知負荷評価の根拠。 |
| CLARE 2024 | 多モーダル負荷推定と10秒自己報告ラベル設計の参考。 |
| CL-Drive 2024 | 現実的操作タスクでの多モーダル認知負荷データ設計の参考。 |
| Medeiros et al. 2024 | EEGを万能な正解でなく、fMRI等と対応する参照軸として扱う根拠。 |
| ScreenAI 2024 / SeeClick 2024 | 画面文脈・UI要素・作業対象をVLM/OCRで説明する技術的根拠。 |
| JumpStarter 2024 | 高負荷停滞区間をタスク分解・文脈整理へ接続する根拠。 |

## 10. Next Actions

- `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md` と本メモを対応させ、主要論文を個別要約ファイルに分割する。
- 提案書の「課題・背景」では、集中力を単一スコアとして書かず、「多モーダル潜在状態の変化」として定義する。
- 実験計画では、まず `Z_simple(t) = [W(t), A(t), P(t), C(t)]` を検証する。
- 画面録画/VLMによる `C(t)` の推定について、ScreenAI/SeeClick以外にも screen recording の自動アノテーション研究を追加調査する。
- 評価計画には、分類精度だけでなく、弁別的妥当性、説明妥当性、介入妥当性を入れる。

## User Review

- 見てほしいファイル: `nedo/drafts/2026-06-05_system_problem_decomposition.md`
- 確認してほしい判断: NEDO提案の中心定義を「多モーダル潜在状態 `Z(t)` の変化」として採用してよいか。
- 許可が必要な次の編集: この定義を `nedo/第2回ミーティング決定事項.txt` の「課題・背景」文体に合わせて、提案書下書き用の小段落へ変換すること。
