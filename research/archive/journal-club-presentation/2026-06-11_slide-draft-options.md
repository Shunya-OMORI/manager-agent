# moving mfSSVEP 雑誌会スライド下書き方針

## Summary

先輩資料 `rules/雑誌会template.pdf` は全31枚であり，本編19枚とAppendix 12枚からなる．
本編は「概要，背景，既存方法，課題，提案，提案要素の分解，実験，結果，考察，限界，
まとめ，発表者コメント」という順序である．対象論文でもこの説明上の役割を保てる．

一方，先輩資料は基盤モデル論文であり，対象論文は5ページのパイロット臨床研究である．
そのため，個々のアブレーションをそのまま対応させることはできない．31枚すべてを使う場合は，
Appendixを解析式，統計上の注意，本文内の数値不一致，想定質問に置き換える必要がある．

## Evidence

- 先輩資料: `rules/雑誌会template.pdf`
- ページ別抽出: `research/drafts/journal-club-presentation/senior-journal-club-template_original.md`
- レイアウト確認: `research/drafts/journal-club-presentation/senior-journal-club-template_layout.txt`
- 対象論文: `research/paper_candidates/papers/Novel_Moving_Steady-State_Visual_Evoked_Potential_Stimulus_to_Assess_Afferent_and_Efferent_Dysfunction_in_Multiple_Sclerosis.pdf`
- 全文和訳: `research/drafts/journal-club/moving-mfssvep-ms_ja.md`
- 詳細要約: `research/drafts/journal-club/moving-mfssvep-ms_summary.md`

PDF抽出の標準ツールであるPopplerは実行環境に未導入だったため，今回はPyMuPDFで
ページ別テキストとページ画像を生成し，全31ページを目視した．

## Options

### Option 1: 31枚を厳密に対応させる

先輩資料と同じ31枚を作り，各ページの説明上の役割も合わせる．Appendixも12枚作る．

- 利点: 先輩資料との対応が最も見やすく，レイアウト作成時に迷いにくい．
- 弱点: 5ページの対象論文に対して情報を細分化しすぎ，15分発表では駆け足になりやすい．

### Option 2: 本編19枚を厳密対応，Appendixは論点別に再設計

本編1--19枚は先輩資料の役割と1:1で対応させる．Appendixは枚数を固定せず，
質問されやすい解析式，統計，実験条件，批判的評価だけを置く．

- 利点: 15分発表の流れと先輩資料への対応を両立しやすい．
- 弱点: PDF全体としては31枚の完全対応ではなくなる．

### Option 3: 15分を優先して統合する

先輩資料の順序と情報密度を参考にするが，背景と方法を統合して本編14--16枚程度にする．
Appendixは想定質問への回答だけを用意する．

- 利点: 一枚当たり約50--60秒を確保でき，刺激設計と結果を丁寧に説明できる．
- 弱点: 「各スライドを1:1で対応」という今回の意図から最も離れる．

## Recommendation

Option 2を推奨する．本編19枚は先輩資料とページ単位で対応させ，発表の見通しを保つ．
Appendixは対象論文に実在する論点だけで構成する．本編では論文の主張を説明し，
Appendixでは発表者による検証と批判を扱うことで，両者を混同しにくい．

## Proposed Main Slides

| No. | 先輩資料の役割 | 対象論文での内容 |
| --- | --- | --- |
| 1 | 表紙 | 書誌情報，著者，発表者 |
| 2 | 概要 | 背景，目的，方法，主要結果 |
| 3 | 対象疾患 | 多発性硬化症と視覚系障害 |
| 4 | 既存の解析・検査法 | 視力，VEP，OCT，眼球運動計測の比較 |
| 5 | 対象領域の課題 | 専門設備，別々の検査，可搬性の不足 |
| 6 | 提案手法の全体像 | HMD＋移動mfSSVEP＋EEG/EOG |
| 7 | 提案要素1 | 多焦点SSVEPと求心性指標 |
| 8 | 提案要素2 | 移動刺激と遠心性追従指標 |
| 9 | 同時計測の流れ | 刺激からEEG/EOG指標までの処理 |
| 10 | 実験条件 | 参加者，眼，試行，刺激条件 |
| 11 | 解析方法 | 前処理，DFT，SNR，相関，ANCOVA |
| 12 | 結果の一覧 | SNRと眼球追従性能の群比較 |
| 13 | 結果の詳細1 | mfSSVEP SNRの群差 |
| 14 | 結果の詳細2 | 眼球追従性能に有意差なし |
| 15 | 例示・可視化 | Fig. 3の周波数スペクトルと追従軌跡 |
| 16 | 考察 | 求心性指標の可能性と遠心性結果の解釈 |
| 17 | 限界と今後 | 小標本，EOG干渉，縦断検証，計測時間 |
| 18 | まとめ | 直接示されたことを3--4点に限定 |
| 19 | コメント | 新規性，統計上の懸念，研究室との接点 |

## Proposed Appendix

1. SSVEPとmfSSVEPの基礎
2. 20区画と刺激周波数の割当て
3. 5秒エポックと0.2 Hz周波数分解能
4. SNR式とパターンA/Bの役割
5. 水平EOGと相関係数
6. 参加者情報とEDSS
7. EEG/EOG前処理の詳細
8. ANCOVAと年齢調整
9. AbstractとResultsのSNR数値不一致
10. 左右眼を独立標本として扱うことへの懸念
11. `p = 0.049`と多重比較の扱い
12. 計測時間と実用性

## User Review

- 2026-06-11，ユーザはOption 2を選択した．
- 本編19枚を先輩資料と1:1で対応させ，Appendix 12枚を対象論文固有の論点で構成する．
- スライドとセリフの下書き:
  `research/drafts/journal-club-presentation/moving-mfssvep-ms_slide-script.md`
