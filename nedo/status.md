# NEDO Status

Status: waiting-user

## Current State

第2回ミーティング決定事項を中心に，`nedo/提案書様式.txt` の公開サマリー，審査用資料，審査用補足資料1〜9，参考文献をスライド単位で埋めた下書き `nedo/drafts/2026-06-12_proposal-all-slides.md` を作成した。

確定済みの「1．課題・背景」は変更していない。未確定の数値・仕様・計画は `[仮定]`，チーム固有情報は `[要確認]`，既存研究から導いた判断は `[推論]` として区別した。本文中引用は著者年方式とし，末尾に参考文献スライドを設けた。

市場母集団は総務省統計局の2024年「専門的・技術的職業従事者」1,324万人を用いた。SAMは `[仮定]` 月額1,000円を掛けた約1,589億円/年を検証対象の仮説として記載した。

第2回ミーティング記録をもとに、NEDOシステムを「EEG/生理信号による認知状態推定」「画面・作業ログの記録」「VLM/OCRによる作業文脈理解」「LLMエージェントによるタスク細分化」「レポート生成とTodo更新」に分解した。

この分解と最近の論文候補を最初に `nedo/drafts/2026-06-05_system_problem_decomposition.md` に整理した。

その後、`nedo/壁打ち1.md` の論点に沿って、脳波と画面・操作ログの補完関係、および多モーダルデータで集中力・認知負荷・フローを定義するための先行研究を `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md` に整理した。

さらに、`nedo/drafts/2026-06-05_system_problem_decomposition.md` を再構成し、NEDOの中心課題を「集中力・認知負荷の変化を、多モーダル潜在状態 `Z(t)` の変化としてどのように定義し、評価するか」という問題へ整理し直した。

その後、同ファイルに実装向けの最小モデルを追加し、`Z(t)` を時間窓ごとの特徴量テーブル、スコアベクトル、状態ラベル、変化点検出、JSONレポート入力へ落とし込める形にした。

さらに、6状態それぞれに小さな expert model を置き、最後に軽量な出力層で統合する設計を `nedo/drafts/2026-06-05_statewise_expert_model_design.md` に整理した。

## Next Action

`nedo/drafts/2026-06-12_proposal-all-slides.md` をユーザが確認し，提案タイトル，EEGデバイス，実行体制，倫理審査，研究開発期間，PoC対象者数，知財・実績，SAM価格仮説，データ二次利用の扱いを回答する。

## Blockers

- 正式な提出期限が未記入。
- SAM 1,000 億円以上を支える市場根拠が未調査。
- 集中力変化の定義が未確定。現時点では、操作ログからfocused work候補区間を抽出し、EEG/生理信号で内的負荷・注意・疲労を推定し、画面録画/VLMで要因を説明する多モーダル定義が有力。
- 掲載誌のIF/Q1情報は、Web of Science などで追加確認が必要。

## Latest Outputs

- `nedo/drafts/2026-06-12_proposal-all-slides.md`
- `nedo/research/summaries/2026-06-12-japan-knowledge-worker-market.md`
- `nedo/research/summaries/2026-06-12-ethics-and-privacy.md`
- `nedo/drafts/2026-06-05_system_problem_decomposition.md`
- `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md`
- `nedo/drafts/2026-06-05_statewise_expert_model_design.md`

## Key Files

- Task: `tasks/active/nedo-proposal.md`
- Context: `nedo/context/source_files.md`
- Research URLs: `nedo/research/urls.md`
- Logs: `nedo/logs/`
