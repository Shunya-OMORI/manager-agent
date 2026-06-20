# 区間エピソードデータ形式とGraphRAGの先行研究

## Source

- Title: A stage-based model of personal informatics systems
- URL or PDF: https://doi.org/10.1145/1753326.1753409
- Authors / Organization: Li, Dey, and Forlizzi
- Date: 2010
- Accessed: 2026-06-21
- Source type: paper

- Title: Cognitive Prosthetic: An AI-Enabled Multimodal System for Episodic Recall in Knowledge Work
- URL or PDF: https://doi.org/10.1145/3772363.3798940
- Authors / Organization: Obiuwevwi et al.
- Date: 2026
- Accessed: 2026-06-21
- Source type: paper

- Title: MindMirror: A Local-First Multimodal State-Aware Support System for Digital Workers
- URL or PDF: https://arxiv.org/abs/2605.11700
- Authors / Organization: Luo, Wang, and Wang
- Date: 2026
- Accessed: 2026-06-21
- Source type: preprint

- Title: Lifelog Retrieval From Daily Digital Data: Narrative Review
- URL or PDF: https://pmc.ncbi.nlm.nih.gov/articles/PMC9112086/
- Authors / Organization: Ribeiro, Trifan, and Neves
- Date: 2022
- Accessed: 2026-06-21
- Source type: review

- Title: Multi-modal Time Series Analysis: A Tutorial and Survey
- URL or PDF: https://arxiv.org/abs/2503.13709
- Authors / Organization: Li et al.
- Date: 2025
- Accessed: 2026-06-21
- Source type: preprint / survey

## Reliability

- Reliability: medium-high
- Reason: Personal informatics, CHI, JMIR及びACM系の研究は設計根拠として信頼性が高い．MindMirror及びMulti-modal Time Series AnalysisはarXiv段階であり，設計参考として扱い，確定的な実証根拠としては使わない．

## Summary

個人データを作業改善へ使うには，単に収集するだけでなく，統合，振り返り，行動変容へ接続できる形式にする必要がある．知識労働の支援では，時間同期されたJSON形式のエピソード記録，ローカル保存，手動訂正，構造化内省，日次・週次レビューが近い設計として現れている．一方，時系列データをRAGへ入れる場合は，テキスト要約だけではなく，時間軌跡の特徴量と実際の前後関係を保持する必要がある．

## Useful Claims

- 区間データは，collectionだけでなくreflection/actionに使うことを前提に設計する必要がある．
- 画面，生理信号，視線，発話，テキストなどの異種データは，時間同期されたエピソード記録としてまとめる設計が近い．
- ユーザの手動訂正と承認・拒否履歴は，状態推定の誤りを補正し，個人化に使える重要なデータである．
- 多モーダル時系列は，平均値だけでなく，モダリティ間相互作用，傾き，変動，状態遷移を特徴として扱う必要がある．
- RAGに入れる単位は，テキストチャンクではなく，テキスト，時系列特徴量，証拠ポインタ，結果を持つエピソードノードが適している．

## Limitations

- CPMSは知識労働のエピソード想起に近いが，EEGを中心にしたTodo更新システムではない．
- MindMirrorはデジタルワーカー支援として近いが，arXiv段階であり，顔表情中心でEEGを扱わない．
- Multi-modal Time Series Analysisは一般的な時系列手法の整理であり，本提案のNEDOシステムを直接検証したものではない．
- Lifelog研究は検索・記憶支援には近いが，作業の成果物差分と認知負荷を使ったタスク分解までは扱わない．

## Citation Candidate

- Li, Dey, and Forlizzi (2010), personal informatics.
- Obiuwevwi et al. (2026), CPMS.
- Luo, Wang, and Wang (2026), MindMirror.
- Ribeiro, Trifan, and Neves (2022), lifelog retrieval review.
- Li et al. (2025), multi-modal time series survey.

## Related Task

- `tasks/active/nedo-proposal.md`
