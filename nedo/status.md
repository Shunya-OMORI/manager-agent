# NEDO Status

Status: waiting-user

## Current State

2026-06-14に，`nedo/脳波ポモドーロ_提案書_v2.pptx.txt` を母体として，EEG閾値判定，タスク管理AI，RAG及びローカルモデル発展を詳細化した新規下書き `nedo/drafts/2026-06-14_proposal-threshold-rag-design.md` を作成した。

EEGイベント判定は機械学習分類器を用いず，課題関与 `beta/(alpha+theta)`，前頭theta中心の認知負荷，`(theta+alpha)/beta` による低覚醒方向，前頭alpha非対称性，前頭―頭頂wPLIを個別の軸として扱う。AttentivUの5分較正，0–100正規化，15秒窓，0–30低 engagement 判定を基準方式とし，標準偏差方式及びハイブリッド方式をPoCで比較する。

LLMはEEGを分類せず，検出済みイベントと画面・操作・Todo・成果物を用いて原因説明とタスク細分化を行う。初期は外部LLM APIとRAGを用い，履歴蓄積後はローカルモデルのLoRA追加学習，ユーザ選好に基づくDPO等へ段階的に移行する設計とした。

ユーザ指定の文章ルールに合わせて，2026-06-14版を箇条書き中心に改稿した。4状態の主判定は有効操作活動量と認知負荷の2軸へ限定した。有効操作活動量は，タスクに関連する操作と成果物更新を加点し，無関係な操作と同一操作の反復を減点する。有効操作活動量が高い場合は原則として「順調な集中」とし，低活動区間を認知負荷の低，適正，高によって「作業からの離脱」「低活動だが思考中」「高負荷で停滞」へ分ける。

課題関与指標は介入方法の選択と深い思考の保護に用いる。同期度指標はリアルタイム判定へ用いず，成果との個人内関連が複数回再現した場合だけ，作業後レポートと次回Todo配置へ用いる。

第2回ミーティング決定事項を中心に，`nedo/提案書様式.txt` の公開サマリー，審査用資料，審査用補足資料1〜9，参考文献をスライド単位で埋めた下書き `nedo/drafts/2026-06-12_proposal-all-slides.md` を作成した。

確定済みの「1．課題・背景」は変更していない。未確定の数値・仕様・計画は `[仮定]`，チーム固有情報は `[要確認]`，既存研究から導いた判断は `[推論]` として区別した。本文中引用は著者年方式とし，末尾に参考文献スライドを設けた。

市場母集団は総務省統計局の2024年「専門的・技術的職業従事者」1,324万人を用いた。SAMは `[仮定]` 月額1,000円を掛けた約1,589億円/年を検証対象の仮説として記載した。

第2回ミーティング記録をもとに、NEDOシステムを「EEG/生理信号による認知状態推定」「画面・作業ログの記録」「VLM/OCRによる作業文脈理解」「LLMエージェントによるタスク細分化」「レポート生成とTodo更新」に分解した。

`user-profile.txt` の学部3年前期の学生プロジェクト実績を，チーム概要，遂行能力，計測デバイス候補，参加者詳細，関連研究開発実績へ反映した。ADS1299，XIAO ESP32-S3，Ag/AgCl電極，3Dプリント筐体，Flutter/BLE計測アプリ，RabbitMQ/MNE-Python解析基盤の試作経験を具体化した。

自作 EEG デバイスは今回の確定仕様ではなく採用候補として扱った。過去には既存生体信号アンプとの閉眼時α波，ERP，SSVEP等の同時計測を実施しているが，PSD確認が中心で定量評価は未実施である。そのため，本事業では信号対雑音比，帯域パワー相関，ERP振幅・潜時，SSVEPピーク，試行間再現性を比較する計画とした。

この分解と最近の論文候補を最初に `nedo/drafts/2026-06-05_system_problem_decomposition.md` に整理した。

その後、`nedo/壁打ち1.md` の論点に沿って、脳波と画面・操作ログの補完関係、および多モーダルデータで集中力・認知負荷・フローを定義するための先行研究を `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md` に整理した。

さらに、`nedo/drafts/2026-06-05_system_problem_decomposition.md` を再構成し、NEDOの中心課題を「集中力・認知負荷の変化を、多モーダル潜在状態 `Z(t)` の変化としてどのように定義し、評価するか」という問題へ整理し直した。

その後、同ファイルに実装向けの最小モデルを追加し、`Z(t)` を時間窓ごとの特徴量テーブル、スコアベクトル、状態ラベル、変化点検出、JSONレポート入力へ落とし込める形にした。

過去には，6状態それぞれに小さなexpert modelを置く設計を `nedo/drafts/2026-06-05_statewise_expert_model_design.md` に整理した。2026-06-14の方針変更により，この設計は現行案へ採用せず，4状態の閾値判定を用いる。

## Next Action

`nedo/drafts/2026-06-14_proposal-threshold-rag-design.md` のスライド19から24を確認し，有効操作活動量の定義，認知負荷の3段階閾値，課題関与による介入分岐，同期度による長期Todo配置，電極配置及び外部LLM APIへ送信する情報範囲を確定する。

`nedo/drafts/2026-06-12_proposal-all-slides.md` のスライド7，18，23，27，29をユーザが確認し，自作EEGを採用候補として残すか，参加者の氏名・正式役割，発表題目・開催日・共著者，既存試作物の利用可否を回答する。その後，提案タイトル，倫理審査，研究開発期間，PoC対象者数，知財，SAM価格仮説，データ二次利用を順に確定する。

## Blockers

- 正式な提出期限が未記入。
- SAM 1,000 億円以上を支える市場根拠が未調査。
- 有効操作活動量の算出式と，タスク種別ごとの基準値が未確定。
- 認知負荷の低，適正，高を分けるz得点閾値が未確定。
- 同期パターンをTodo配置へ反映するために必要な反復回数と統計基準が未確定。
- 掲載誌のIF/Q1情報は、Web of Science などで追加確認が必要。
- 自作 EEG 試作物，設計データ，アプリ・サーバのソースコード，比較計測環境が現在利用可能か未確認。
- 第9回合同シンポジウムの正式な発表題目，開催日，共著者が未確認。

## Latest Outputs

- `nedo/drafts/2026-06-14_proposal-threshold-rag-design.md`
- `nedo/drafts/2026-06-14_four-state-threshold-design.md`
- `nedo/research/summaries/2026-06-14_attentivu-threshold.md`
- `nedo/research/summaries/2026-06-14_eeg-indicators.md`
- `nedo/research/summaries/2026-06-14_task-ai-and-llm-architecture.md`

- `nedo/drafts/2026-06-12_proposal-all-slides.md`
- `nedo/research/summaries/2026-06-12-japan-knowledge-worker-market.md`
- `nedo/research/summaries/2026-06-12-ethics-and-privacy.md`
- `nedo/research/summaries/2026-06-12_ads1299-specifications.md`
- `nedo/research/summaries/2026-06-12_ads1299-eeg-validation.md`
- `nedo/drafts/2026-06-05_system_problem_decomposition.md`
- `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md`
- `nedo/drafts/2026-06-05_statewise_expert_model_design.md`

## Key Files

- Task: `tasks/active/nedo-proposal.md`
- Context: `nedo/context/source_files.md`
- Research URLs: `nedo/research/urls.md`
- Logs: `nedo/logs/`
