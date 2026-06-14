# 時系列エピソード遷移グラフとRAG

## Source

- Title: EventRAG: Enhancing LLM Generation with Event Knowledge Graphs
- URL or PDF: https://aclanthology.org/2025.acl-long.830/
- Authors / Organization: Huang et al.
- Date: 2025
- Accessed: 2026-06-15
- Source type: paper

- Title: ScreenTrack: Using a Visual History of a Computer Screen to Retrieve Documents and Web Pages
- URL or PDF: https://dl.acm.org/doi/10.1145/3313831.3376753
- Authors / Organization: Cheng et al.
- Date: 2020
- Accessed: 2026-06-15
- Source type: paper

- Title: Entity-Event Knowledge Graph for Retrieval-Augmented Generation
- URL or PDF: https://aclanthology.org/2026.eacl-long.90/
- Date: 2026
- Accessed: 2026-06-15
- Source type: paper

## Reliability

- Reliability: high
- Reason: ACL，EACL及びCHIの査読論文を用いた．本提案への適用部分は，論文の手法を作業ログへ転用した設計上の推論である．

## Summary

通常のベクトルRAGは意味的に近い断片を検索できるが，イベント間の時間順序及び論理的な接続を直接保持しない．EventRAG及びEntity-Event Knowledge Graphは，イベントをノードとし，時間的又は論理的な関係をエッジとして保持することで，複数イベントにまたがる検索と推論を行う．ScreenTrackは，PC画面の視覚的な履歴が，中断前の文脈の再構成とタスク復帰に利用できることを示す．

## Useful Claims

- 作業ログは，独立した文書断片ではなく，時間順序を持つイベント列として保存する必要がある．
- 意味類似度による近傍関係と，実際に観測された前後関係は，別のエッジとして保持する必要がある．
- 現在に似たエピソードを検索した後，時間エッジを複数ステップたどることで，停滞から回復した過去経路を取得できる．
- 画面履歴，作業文脈及び中断時点を保存することは，タスク復帰支援に利用できる．

## Limitations

- 先行研究は，本提案と同じEEG，操作ログ及び成果物を統合した作業支援を直接検証したものではない．
- 2次元射影上の距離は元の高次元距離を歪めるため，検索には使用しない．
- 類似する回復経路の検索は関連例を示すものであり，介入の因果効果を証明しない．
- 工数予測には，タスクの完了基準と十分な数の完了軌跡が必要である．

## Citation Candidate

- Huang et al. (2025), EventRAG.
- Cheng et al. (2020), ScreenTrack.
- Entity-Event Knowledge Graph for RAG (2026).

## Related Task

- `tasks/active/nedo-proposal.md`
