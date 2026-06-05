# NEDO Status

Status: researching

## Current State

第2回ミーティング記録をもとに、NEDOシステムを「EEG/生理信号による認知状態推定」「画面・作業ログの記録」「VLM/OCRによる作業文脈理解」「LLMエージェントによるタスク細分化」「レポート生成とTodo更新」に分解した。

この分解と最近の論文候補を最初に `nedo/drafts/2026-06-05_system_problem_decomposition.md` に整理した。

その後、`nedo/壁打ち1.md` の論点に沿って、脳波と画面・操作ログの補完関係、および多モーダルデータで集中力・認知負荷・フローを定義するための先行研究を `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md` に整理した。

さらに、`nedo/drafts/2026-06-05_system_problem_decomposition.md` を再構成し、NEDOの中心課題を「集中力・認知負荷の変化を、多モーダル潜在状態 `Z(t)` の変化としてどのように定義し、評価するか」という問題へ整理し直した。

その後、同ファイルに実装向けの最小モデルを追加し、`Z(t)` を時間窓ごとの特徴量テーブル、スコアベクトル、状態ラベル、変化点検出、JSONレポート入力へ落とし込める形にした。

さらに、6状態それぞれに小さな expert model を置き、最後に軽量な出力層で統合する設計を `nedo/drafts/2026-06-05_statewise_expert_model_design.md` に整理した。

## Next Action

`nedo/drafts/2026-06-05_statewise_expert_model_design.md` を確認し、6 expert model の方針で進めるか判断する。最初の実装候補は `stuck`, `thinking`, `switching` の3 expert。

## Blockers

- 正式な提出期限が未記入。
- SAM 1,000 億円以上を支える市場根拠が未調査。
- 集中力変化の定義が未確定。現時点では、操作ログからfocused work候補区間を抽出し、EEG/生理信号で内的負荷・注意・疲労を推定し、画面録画/VLMで要因を説明する多モーダル定義が有力。
- 掲載誌のIF/Q1情報は、Web of Science などで追加確認が必要。

## Latest Outputs

- `nedo/drafts/2026-06-05_system_problem_decomposition.md`
- `nedo/drafts/2026-06-05_multimodal_cognitive_state_definition.md`
- `nedo/drafts/2026-06-05_statewise_expert_model_design.md`

## Key Files

- Task: `tasks/active/nedo-proposal.md`
- Context: `nedo/context/source_files.md`
- Research URLs: `nedo/research/urls.md`
- Logs: `nedo/logs/`
