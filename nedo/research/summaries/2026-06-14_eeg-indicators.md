# EEG 指標5種の根拠と利用制限

## Source

- Pope et al. 1995: https://pubmed.ncbi.nlm.nih.gov/7647180/
- Chikhi et al. 2022: https://doi.org/10.1111/psyp.14009
- Jap et al. 2009: https://doi.org/10.1016/j.eswa.2007.12.043
- Sabu et al. 2022: https://doi.org/10.3389/fcomp.2022.869123
- Stam et al. 2007: https://doi.org/10.1002/hbm.20346
- Vinck et al. 2011: https://doi.org/10.1016/j.neuroimage.2011.01.055
- Accessed: 2026-06-14
- Source type: papers

## Reliability

- Reliability: high
- Reason: engagement indexの原報，認知負荷メタ分析，前頭α非対称性レビュー，接続性指標の方法論文を使用した．

## Summary

課題関与には `beta / (alpha + theta)`，認知負荷には前頭θ，低覚醒・疲労方向には `(theta + alpha) / beta`，接近・回避傾向には前頭α非対称性，部位間同期にはwPLIを候補とする．

認知負荷メタ分析では前頭θが最も一貫していた．FAAは単純な快不快より接近・回避動機として解釈する方が妥当である．通常のコヒーレンスは体積伝導に弱いため，wPLIを優先する．

## Useful Claims

- 5指標を別軸として保持することで，集中，負荷，覚醒，情動，ネットワーク同期の混同を減らせる．
- FAAとwPLIは初期段階では単独介入トリガーにせず，レポートと探索的解析へ用いるべきである．
- EEG指標は作業文脈を調べるイベントトリガーであり，心理状態の正解ラベルではない．

## Limitations

- 指標間で周波数帯が重複する．
- 電極配置，参照方式，課題，時間経過，個人差，アーティファクトにより値が変化する．
- 同期増加が常に良い状態を意味するわけではない．

## Related Task

- `tasks/active/nedo-proposal.md`
