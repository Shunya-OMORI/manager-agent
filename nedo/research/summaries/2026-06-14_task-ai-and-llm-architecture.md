# タスク管理AIと段階的LLM個人化の設計根拠

## Source

- Motion: https://www.usemotion.com/help/time-management/auto-scheduling
- Reclaim: https://help.reclaim.ai/en/articles/8291694-how-reclaim-uses-priorities-to-intelligently-plan-your-workweek
- Sunsama: https://help.sunsama.com/docs/usage-guides/timeboxing/
- Todoist: https://www.todoist.com/help/articles/use-the-task-assist-extension-with-todoist-ZgldtcPeT
- Lewis et al. 2020: https://arxiv.org/abs/2005.11401
- Wang et al. 2023: https://doi.org/10.18653/v1/2023.acl-long.147
- Hu et al. 2021: https://arxiv.org/abs/2106.09685
- Rafailov et al. 2023: https://arxiv.org/abs/2305.18290
- Accessed: 2026-06-14
- Source type: official product documents / papers

## Reliability

- Reliability: high for disclosed product behavior and paper methods
- Reason: 製品の内部実装は非公開だが，ユーザが設定する入力と公開動作は公式資料で確認できる．LLM部分は一次論文を用いた．

## Summary

既存製品は，タスク，締切，優先度，所要時間，カレンダー空き時間を構造化し，時間枠へ配置し，変更時に再配置する．LLMはタスク抽出や細分化へ利用できるが，厳密な時間制約は決定論的スケジューラへ分離する方が安全である．

初期個人化は，過去のEEGイベント，作業文脈，介入，結果を検索するRAGで実現する．データが蓄積した後は，ユーザ修正済み提案によるLoRA教師あり学習，選択・拒否ペアによるDPO等へ進める．

## Useful Claims

- 外部LLM APIでもRAGにより更新可能な個人履歴を利用できる．
- LLMは候補生成，スケジューラは制約検証，ユーザは最終承認という責務分離ができる．
- EEG値を直接報酬とせず，明示選択，完了，成果物を主報酬とする必要がある．

## Limitations

- Motion等の内部アルゴリズムは公開されていないため，公開機能からの設計上の推論である．
- 個人ごとのモデル追加学習には，十分な件数，品質，利用同意，忘却・削除手順が必要である．

## Related Task

- `tasks/active/nedo-proposal.md`
