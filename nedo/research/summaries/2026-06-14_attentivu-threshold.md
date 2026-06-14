# AttentivU の個人較正と閾値判定

## Source

- Title: AttentivU: An EEG-Based Closed-Loop Biofeedback System for Real-Time Monitoring and Improvement of Engagement for Personalized Learning
- URL: https://doi.org/10.3390/s19235200
- Authors: Nataliya Kosmyna, Pattie Maes
- Date: 2019
- Accessed: 2026-06-14
- Source type: paper

## Reliability

- Reliability: high
- Reason: 査読付き原著論文であり，算出式，較正，閾値，介入条件が本文に明示されている．

## Summary

EEG engagement index `E = beta / (alpha + theta)` を用いて学習中の課題関与を監視し，低下時に振動刺激を与える閉ループシステムである．

5分間の個人較正から `E_min` と `E_max` を求め，平滑化した値を0–100へ正規化する．0–30を低，31–70を中，71–100を高とし，低状態が15秒以上続いた場合に振動を提示した．

## Useful Claims

- 文献と同じ0–100表示及び0–30閾値を基準実装として再現できる．
- 15秒窓と持続条件を用いることで，瞬間的な変動による誤介入を抑えている．
- 個人ごとの較正が必要であり，固定された生の比率を全員へ適用していない．

## Limitations

- 講義視聴を対象としており，自由なナレッジワークとは異なる．
- 最小値と最大値は外れ値の影響を受ける．
- engagement indexは覚醒，負荷，筋電等の影響を受けうるため，心理状態を一意に決めない．

## Related Task

- `tasks/active/nedo-proposal.md`
