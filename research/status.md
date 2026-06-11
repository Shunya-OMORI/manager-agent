# Research Status

Status: waiting-user

## Current State

2026-06-11、雑誌会で紹介する論文を
「Novel Moving Steady-State Visual Evoked Potential Stimulus to Assess
Afferent and Efferent Dysfunction in Multiple Sclerosis」に決定した。
原文テキスト、全文和訳、詳細要約の下書きは作成済み。
ほかの候補論文の成果物は比較資料として保持している。

先輩の雑誌会資料31枚をページ別に抽出・目視し，本編19枚とAppendix 12枚の
説明上の役割を整理した。ユーザは，本編19枚を1:1で対応させ，
Appendixを対象論文固有の論点で再設計するOption 2を選択した。

本編19枚とAppendix 12枚について，表示文，図のテキスト表現，
読み上げるセリフ，設計意図を記した下書きを作成した。

論文読解資料と発表資料の責務を分けるため，発表構成，スライド原稿，
先輩資料の分析結果は`research/drafts/journal-club-presentation/`を
正規の作業場所とする。

ユーザの指摘に基づき，スライド原稿を全面改稿した。
専門用語を最初から理解していることを前提にせず，平易な説明の後で
`MS`，求心性・遠心性，`EOG`，`SSVEP`，`mfSSVEP`，`SNR`を導入する。
低コントラスト視力，`OCT`，サッカード，smooth pursuitも初出時に説明した。

本編19枚は，先輩資料の「表紙，概要，対象疾患，既存検査，課題，提案，
提案要素の分解，実験，解析，結果，考察，限界，まとめ，コメント」という
ページ役割へ再度1:1で整列した。表紙には図を置かず，論文投稿時の著者所属を
記載する。概要，まとめ，コメントも先輩資料と同様に文章中心とした。
各スライドには，図の要否と前後をつなぐ読み上げ文を記載した。

追加のユーザ指摘と`rules/slide-rules.txt`，`rules/japanese_rules.txt`，
`rules/paper-rules.txt`に基づき，表示文とセリフを再改稿した。
スライド上は`MS`，セリフ上は「多発性硬化症」に統一した。
「略してmfSSVEP」のような略称導入自体の説明と，
一般的な用語ではない「脳波応答」「脳波指標」を削除した。

各スライドのタイトルをキーポイントへ変更し，比較結果には比較対象を明記した。
概要の結果は，mfSSVEP SNRと眼球追従性能を別項目に分けた。
図を置かないスライドは，前ページを見返さなくても内容を理解できる情報量へ増やした。
`slide-rules.txt`の「最後のページは結論」に従い，
Slide 18をコメント，Slide 19を結論へ変更した。

Slide 1とSlide 2について，追加のユーザ指摘を反映した。
Slide 1のセリフは論文紹介と研究目的の2文に絞った。
略語の初出は「多発性硬化症（multiple sclerosis，MS）」とし，
Slide 2の冒頭で疾患を説明してから研究概要へ進む構成に変更した。
機能には「評価」，EEGとEOGには「記録」を用い，
「異なる検査装置」は比較対象を誤読しない「複数の検査装置」へ変更した。

Slide 2--4について，追加のユーザ指摘を反映した。
Slide 2では未導入の「求心性機能」「遠心性機能」を使わず，
眼から脳への視覚情報の伝達と脳から眼への運動指令を「二方向の視覚機能」と表現した。
課題の後に研究目的を置き，方法，求心性側の結果，遠心性側の結果を
「この目的のために」「その結果」「一方」で接続した。
Slide 3では，研究が経路自体を評価したという表現を削除し，
求心性視覚経路と遠心性視覚経路の名称と方向を順に説明した。
Slide 4は検査ごとの5行表へ変更し，論文に明記された
「装置の多くが大型で移動できない」と「二方向を一度に評価できない」を
提案法との主要な対比として示した。

本編19枚とAppendix 12枚について，表示文，セリフ，前後接続を再点検した。
`rules/japanese_rules.txt`に従い，主語と述語の対応，複文内の主語の切替え，
指示語と接続詞が示す論理関係を修正した。
多発性硬化症を髄鞘を損傷する動作主体とはせず，
「多発性硬化症では髄鞘が損傷する」と記述した。
同様に，視覚経路そのものを計測・評価したと誤読される表現を避け，
実際に記録したEEG・EOGと，そこから取得した評価値を主語として明示した。

Slide 4は，既存検査を一律に同時評価不能と断定せず，
一つの検査では二方向を評価できないことと，
装置の多くを患者の場所へ運びにくいことを分けて示した。
Slide 5からSlide 6への接続文を追加し，必要条件から装置構成へ進む流れを明示した。
Slide 7--9は，点滅，SSVEP，mfSSVEP，SNRの順に用語を導入し，
移動刺激，EOG，相関係数の説明と合流させた。
Slide 10--19は，実験，解析，結果一覧，個別結果，代表例，
実証範囲，限界，発表者コメント，結論の順で連続する構成を確認した。
最終ページを除く18枚すべてに次ページへの接続文がある。

Slide 2の冒頭は，疾患の定義と視覚系への影響を二文に分けた。
第一文で，多発性硬化症を「脳や脊髄などの中枢神経に障害が生じる疾患」
と定義する。第二文では「この疾患では」を受け，
視覚情報の伝達と眼への運動指令の両方が損なわれることを説明する。
髄鞘損傷の具体的な説明はSlide 3に残した。

Slide 3には，髄鞘損傷に至る直接的な機序として，
免疫系が中枢神経の髄鞘を攻撃することを追加した。
一方，その免疫反応が始まる根本的な発症原因は未解明であることも明示し，
直接的な機序と疾患の根本原因を区別した。
さらに，求心性視覚経路と遠心性視覚経路を定量評価する意義を，
患者の視覚障害の多面的な把握，病態評価，治療効果のモニタリングとして
Slide 3のセリフに追加した。対象論文は治療法の選択を実証していないため，
「適切な治療を可能にする」とは記載しない。

原論文のIntroductionを再確認し，Slide 1--5の課題設定を改稿した。
中心課題は装置数の多さではなく，精密な視覚機能評価が専門施設に限られ，
求心性機能と遠心性機能の両方を定量評価できる施設がさらに少ないことである。
Slide 1から，二つの機能を一つの検査へまとめる必要性と，
その検査を患者のいる場所へ持っていく狙いを示した。
Slide 4は検査内容の列挙から，既存検査の利点と実用上の制約を対比する表へ変更した。
口頭原稿では「可搬性」「可搬型」を避け，「患者のいる場所へ持っていける」と表現した。

専門施設の少なさを割合で示せるか調査した。
米国では三次医療施設を全国一律に数える公的分類を確認できなかった。
AAMC加盟の教育医療システムと教育病院が米国の全病院の約5%を占めるという
公式資料はあるが，AAMC加盟施設と三次医療施設は同義ではない。
この値を使う場合は，高度専門医療を担う施設群の近似値であり，
対象検査を実施できる施設の割合ではないことを明示する必要がある。

対象論文の参考文献まで追跡した。
「両方を正確に定量化できる施設は少ない」という要旨の文自体には引用がない。
Introductionで設備と専門性の根拠として引用されるGraves et al. (2022)にも，
三次医療施設の割合や両機能を評価できる施設数は記載されていない。
関連するIMSVISUALの調査では世界47施設から回答を得ているが，
各施設が両機能を測定できるかは報告されていない。
したがって，施設数または割合を根拠付きでスライドへ追加することは現時点ではできない。
AAMCの約5%も対象検査の利用可能性を示さないため，本件の根拠には使用しない。

## Next Action

表現規則に基づいて再改稿した
`research/drafts/journal-club-presentation/moving-mfssvep-ms_slide-script.md`を
ユーザが確認する。特にSlide 3の疾患説明，Slide 4--6の
既存検査から提案システムへの接続，Slide 7--9の用語導入，
Slide 12--16の結果と解釈の区別，Slide 19の結論を確認対象とする。
施設割合は追加せず，原論文の定性的な主張として扱うか，
「論文は施設数を示していない」と注記するかをユーザが判断する。
確認後，許可を得て実際のスライド形式へ移す。

## Blockers

- 全スライドの再改稿後の表示文とセリフについて，ユーザの確認が必要。
- 発表日が未確認。

## Latest Outputs

- `research/drafts/journal-club/eeg-glasses_original.md`
- `research/drafts/journal-club/eeg-glasses_layout.txt`
- `research/drafts/journal-club/eeg-glasses_pdfinfo.txt`
- `research/drafts/journal-club/eeg-glasses_ja.md`
- `research/drafts/journal-club/eeg-glasses_summary.md`
- `research/drafts/journal-club/real-time-eeg-cwm_original.md`
- `research/drafts/journal-club/real-time-eeg-cwm_ja.md`
- `research/drafts/journal-club/real-time-eeg-cwm_summary.md`
- `research/drafts/journal-club/moving-mfssvep-ms_original.md`
- `research/drafts/journal-club/moving-mfssvep-ms_ja.md`
- `research/drafts/journal-club/moving-mfssvep-ms_summary.md`
- `research/drafts/journal-club-presentation/README.md`
- `research/drafts/journal-club-presentation/senior-journal-club-template_original.md`
- `research/drafts/journal-club-presentation/senior-journal-club-template_layout.txt`
- `research/drafts/journal-club-presentation/senior-journal-club-template_pdfinfo.txt`
- `research/drafts/journal-club-presentation/2026-06-11_slide-draft-options.md`
- `research/drafts/journal-club-presentation/moving-mfssvep-ms_slide-script.md`

## Key Files

- Task: `tasks/active/journal-paper-selection.md`
- Context: `research/context/source_files.md`
- Candidate URLs: `research/paper_candidates/urls.md`
- PDF workflow: `workflows/pdf-to-markdown.md`
- PDF extraction script: `scripts/pdf_to_markdown.py`
- Logs: `research/logs/`
