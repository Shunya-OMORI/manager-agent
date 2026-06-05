# 多モーダルデータによる集中力・認知負荷・フロー定義の先行研究整理

## Summary

今回のNEDOシステムで最も重要な未解決点は、「集中力や認知負荷の変化をどのように定義するか」である。単純に EEG の `beta / (alpha + theta)` が閾値を超えた、という単一指標で判定すると、脳内状態の変化は拾えても、作業が進んでいるのか、止まって考えているのか、画面上で何が詰まりになっているのかを説明しきれない。

先行研究から見ると、EEG・視線・顔・EDA/ECG・操作ログ・画面録画は、互いに代替関係ではなく補完関係にある。

- EEG/生理信号: 手が止まっている時でも、考えている・負荷が高い・疲労している可能性を拾える。
- 操作ログ: キー入力、マウス、アプリ遷移、IDE操作から、作業の継続性・中断・速度・成果に近い行動を拾える。
- 画面録画/画面理解: どのタスク、どの文脈、どのUI、どのエラーや文書が負荷の要因だったかを説明する。
- 視線/顔/姿勢: 画面を見ているか、どこを見ているか、情動やエンゲージメントがどう変化したかを補助する。

したがって、NEDO提案では「集中力変化」を単一生理指標の閾値超過として定義するより、次のように定義する方が研究的に強い。

> 集中力・認知負荷・フローの変化とは、EEG/生理信号に表れる内的状態、画面/操作ログに表れる作業行動、作業成果や自己報告に表れる主観・結果の間に生じる時系列的な変化であり、各モダリティを同期して推定・説明する対象である。

## Cross-Paper Findings

| 論点 | 先行研究から言えること | NEDOで使える形 |
| --- | --- | --- |
| 操作ログだけでフローを定義できるか | Brown et al. 2023 は focused work はログから近似できるが、flow 単体は主観性が強くログだけでは難しいと整理した。 | 操作ログは「集中作業の候補区間」を作るが、flow/集中の弁別にはEEGや自己報告を併用する。 |
| 操作ログと視線は何が違うか | Kevic et al. 2015 は、IDE操作ログと視線が異なる側面を捉え、視線は操作されていないコード要素への注意も捉えると示した。 | キー/マウスが止まっている時間を「非作業」とせず、視線やEEGで「読んでいる/考えている」を補足する。 |
| 生理信号は作業難易度を測れるか | Fritz et al. 2014 は EEG/視線/EDA でソフトウェア課題難易度を分類した。 | タスクの主観的難しさや負荷を、行動ログとは別の内的状態としてモデルに入れる。 |
| 開発者の感情・進捗・フローは測れるか | Müller and Fritz 2015 は生体センサで正/負感情と高/低進捗を分類し、感情と進捗を分けて扱った。 | 「高負荷だが進捗あり」「高負荷で停滞」「低負荷で順調」など、レポートの状態カテゴリを分けられる。 |
| 画面録画を含む多モーダルは有効か | Guntz et al. 2017、Hamed et al. 2026 は画面録画・視線・顔・操作イベントを統合し、単一モダリティより文脈理解に強いことを示す。 | 変化点の要因同定に画面録画/VLMを使う根拠になる。 |
| 認知負荷の正解ラベルはどう作るか | CLARE 2024、CL-Drive 2024 は複数生理信号と視線を同期し、10秒ごとの自己報告を ground truth にした。 | NEDOでも一定間隔の軽い自己報告、作業成果、操作ログを組み合わせたラベル設計が必要。 |
| EEGは ground truth になるか | Medeiros et al. 2024 は fMRI と同期し、EEG特徴が insula 活動と相関する可能性を検証した。 | EEGを万能な正解ではなく、他のウェアラブル指標を検証する参照信号として扱う。 |

## Paper Notes

### 1. Brown et al. 2023: Using Logs Data to Identify When Software Engineers Experience Flow or Focused Work

URL: https://research.google/pubs/using-logs-data-to-identify-when-software-engineers-experience-flow-or-focused-work/  
arXiv: https://arxiv.org/abs/2304.04711  
Venue: CHI 2023  

#### (1) 解こうとしている問題

ソフトウェアエンジニアが「flow」または「focused work」を経験している時間を、自己報告だけに頼らず、日常の作業ログから非侵襲的に推定できるかを扱う。

NEDOとの関係では、「画面・操作ログから集中状態をどこまで定義できるか」を直接考える代表研究である。

#### (2) 既存方法の限界とアプローチ

既存のflow研究は自己報告に依存しやすい。Brown, D'Angelo, Holtz, Jaspan, and Green (2023) は、flowを直接ログで測るのではなく、flowの前提条件に近い focused work をログから測る方向へ問題設定をずらした。

壁打ちで重要なのはここで、論文は「同じようなログパターンでも、本人がflowと感じるかは違う」ため、ログだけでflow単体を測るのは現時点では難しい、と述べている。これはNEDOの「操作ログだけでは、手が止まって考えているのか、集中が切れているのかわからない」という主張を補強する。

#### (3) 実験/解析方法のポイント

大手テック企業内の作業ログを使い、IDE編集、文書閲覧、ビルドなどの関連行動のまとまりから focused work metric を設計した。日記研究と四半期ごとの縦断調査に対して検証している。

#### (4) 解析方法だと何がわかるか

数学的には、ログ上の一連の行動が「関連した作業の連続区間」として自己報告の focused work/flow と一致するかを見る。自己報告との一致度が高ければ、操作ログから focused work の候補区間を抽出できたといえる。

#### (5) 結果と解釈

ソフトウェアエンジニアの focused work はログから推定可能で、flowを含む集中作業の近似指標になりうる。一方で、flowそのものは主観性が強く、ログ単独では切り分けが難しい。

#### (6) 議論・結論

期待通りの側面は、ログから日常作業中の集中作業を非侵襲的に推定できる点。足りない側面は、flowの肯定的情動・没入感・主観的経験をログだけでは扱えない点。NEDOではここにEEG/生理信号と自己報告を足す必然性がある。

### 2. Kevic et al. 2015: Tracing Software Developers' Eyes and Interactions for Change Tasks

URL: https://hasel.dev/publication/tracing-software-developers-eyes-and-interactions-for-change-tasks/  
PDF: https://cs.unibg.it/esecfse_proceedings/fse15/p202-kevic.pdf  
Venue: ESEC/FSE 2015  

#### (1) 解こうとしている問題

開発者が現実的な変更タスク中に、どのコードを見て、どこを操作し、どのようにナビゲートしているかを細かく理解する問題。

#### (2) 既存方法の限界とアプローチ

既存研究は小さなコード断片や粗いIDE操作ログに限られがちだった。Kevic, Walters, Shaffer, Sharif, Shepherd, and Fritz (2015) は、MylynによるIDE操作ログと、iTraceによる細粒度視線データを自動的にソースコード要素へ紐づけることで、この限界を超えようとした。

#### (3) 実験/解析方法のポイント

12名のプロ開発者と10名の学生開発者が、JabRefの3つの変更タスクに取り組んだ。各参加者は合計60分、Eclipse IDE 上で作業し、視線とIDEインタラクションを同時に記録した。技術的問題により一部のタスク調査は除外され、最終的に55件の変更タスク調査が解析対象になった。

#### (4) 解析方法だと何がわかるか

操作ログは「選択・編集・ナビゲーションしたコード」を示す。一方、視線は「操作していないが読んでいる/注意を向けているコード」を示す。両者の上位メソッド一致率や注視時間、メソッド内の読まれた行の割合を見ることで、操作ログだけでは欠ける注意情報がわかる。

#### (5) 結果と解釈

視線データは操作ログとは異なる側面を捉えた。開発者はメソッド全体ではなく、データフローに関係する小さな部分に集中していた。操作ログだけでは「読んでいるが操作していない」箇所が落ちる。

#### (6) 議論・結論

期待通りの側面は、視線と操作ログの統合で現実的変更タスクの細粒度理解が進む点。足りない側面は、内的な負荷や情動までは視線/操作だけでは直接わからない点。NEDOではここにEEGを足すことで、「見ているが詰まっている」「見ていて理解が進んでいる」を分ける余地がある。

### 3. Konopka 2015: Combining Eye Tracking with Navigation Paths for Identification of Cross-Language Code Dependencies

URL: https://kinit.sk/publication/combining-eye-tracking-with-navigation-paths-for-identification-of-cross-language-code-dependencies/  
PDF: https://cs.unibg.it/esecfse_proceedings/fse15/p1057-konopka.pdf  
Venue: ESEC/FSE 2015 Student Research Competition  

#### (1) 解こうとしている問題

静的解析だけでは見つけにくい、異なるプログラミング言語間のコード依存関係を、開発者の視線とナビゲーション行動から発見できるか。

#### (2) 既存方法の限界とアプローチ

従来の依存関係抽出は構文解析や静的解析に依存するが、クロス言語や外部サービス連携では限界がある。Konopka (2015) は、開発者が実際にどの領域を見て、どの順序で移動するかを implicit feedback として使う。

#### (3) 実験/解析方法のポイント

この論文は研究計画・短報に近く、実作業データで評価する計画が中心。視線から area-of-interest を抽出し、IDE内ナビゲーションパスと組み合わせる。

#### (4) 解析方法だと何がわかるか

あるコード要素Aを見た後に要素Bへ移動し、それが複数回・複数人で現れるなら、静的解析で明示されない依存関係の候補と見なせる。

#### (5) 結果と解釈

実証結果よりも方法提案の色が強い。NEDOで重要なのは、作業者の視線・ナビゲーションが「画面上の成果物の隠れた関係」を明らかにするデータになりうる点。

#### (6) 議論・結論

足りない側面は、認知負荷や集中状態を測っていないこと。期待できる側面は、画面/操作ログが単なる活動量ではなく、作業文脈・作業対象間の関係を表せること。

### 4. Fritz et al. 2014: Using Psycho-Physiological Measures to Assess Task Difficulty in Software Development

URL: https://www.microsoft.com/en-us/research/publication/using-psycho-physiological-measures-to-assess-task-difficulty-in-software-development/  
DOI: https://doi.org/10.1145/2568225.2568266  
Venue: ICSE 2014  

#### (1) 解こうとしている問題

開発者が作業中に難しいタスクへ直面しているかを、作業後のバグや自己申告ではなく、作業中の生理信号から推定できるか。

#### (2) 既存方法の限界とアプローチ

既存のバグ予測は、事後的なコード変更・バグ修正履歴に依存する。Fritz, Begel, Müller, Yigit-Elliott, and Züger (2014) は、開発者が困難を経験している瞬間を EEG、視線、EDA で検出し、バグ混入前に支援する方向へ問題設定を変えた。

#### (3) 実験/解析方法のポイント

15名のプロプログラマがコード理解課題を行い、eye tracker、electrodermal activity sensor、EEG sensor を装着した。難易度が異なる課題について、個人をまたぐ予測、新しいタスクへの予測、スライディングウィンドウでの解析が行われた。

#### (4) 解析方法だと何がわかるか

分類器が easy/difficult のラベルを十分な precision/recall で予測できれば、生理信号が作業難易度の情報を持つといえる。55秒程度の窓で性能改善が見られるなら、作業中の連続推定に近づく。

#### (5) 結果と解釈

新しい開発者に対する名目難易度分類で precision 64.99%、recall 64.58%、新しいタスクに対して precision 84.38%、recall 69.79% が報告されている。視線データのみや55秒窓の利用で性能改善が見られた。

#### (6) 議論・結論

期待通りの側面は、生理信号で作業中の難しさを推定できる可能性。足りない側面は、分類性能が完璧ではなく、自由なナレッジワークや長時間作業にそのまま適用できるか不明な点。NEDOでは、作業ログ/画面文脈で補完する必要がある。

### 5. Müller and Fritz 2015: Stuck and Frustrated or In Flow and Happy

URL: https://doi.org/10.1109/ICSE.2015.334  
ResearchGate preview: https://www.researchgate.net/publication/278747629_Stuck_and_Frustrated_or_In_Flow_and_Happy_Sensing_Developers%27_Emotions_and_Progress  
Venue: ICSE 2015  

#### (1) 解こうとしている問題

開発者が変更タスク中に「詰まっていて不満」なのか、「フローに入っていて良い気分」なのか、感情と進捗を生体信号で推定できるか。

#### (2) 既存方法の限界とアプローチ

開発者支援は、作業状態や割り込み可能性を文脈として扱う必要があるが、従来は主観報告や観察に依存していた。Müller and Fritz (2015) は、EEGヘッドバンド、Empaticaリストバンド、視線/画面環境を用いて、正/負の感情と高/低進捗を分類する。

#### (3) 実験/解析方法のポイント

17名の参加者が2つの変更タスクに取り組み、3種類の生体センサを装着した。参加者は定期的に感情と進捗を自己評価した。

#### (4) 解析方法だと何がわかるか

分類器が positive/negative emotion と high/low progress を分けられるなら、「気分」と「進捗」を異なる軸として扱える。NEDOでは、集中力変化を単一軸ではなく、負荷・情動・進捗の組み合わせとして定義する根拠になる。

#### (5) 結果と解釈

正/負感情を 71.36%、低/高進捗を 67.70% で弁別できたと報告されている。感情と進捗は関連するが同一ではない。

#### (6) 議論・結論

期待通りの側面は、開発者の作業状態を生体信号から推定し、割り込みや推薦のタイミング制御に使える可能性。足りない側面は、実験室の変更タスクであり、画面録画の内容理解や成果物品質の自動評価までは入っていない点。

### 6. Guntz et al. 2017: Multimodal Observation and Interpretation of Subjects Engaged in Problem Solving

URL: https://arxiv.org/abs/1710.04486  
Venue: 1st Workshop on Behavior, Emotion and Representation, 2017  

#### (1) 解こうとしている問題

画面上の問題解決中に、視線、姿勢、感情、その他生理信号を統合して、被験者の認知状態や専門性を推定できるか。

#### (2) 既存方法の限界とアプローチ

単一モダリティでは、注意・姿勢・情動の一部しか見えない。Guntz, Balzarini, Vaufreydaz, Crowley et al. (2017) は、チェス問題解決を題材に、Kinect、視線、マウスクリックが重畳された画面録画、webcam顔/感情などを統合した。

#### (3) 実験/解析方法のポイント

難しいチェス問題を解く被験者を観測し、専門性判定を行った。画面ベースの問題解決に対する再現可能な観測装置の検証という側面がある。

#### (4) 解析方法だと何がわかるか

単一モダリティと多モーダルの分類精度を比較し、多モーダルの方が高ければ、複数信号が相補的情報を持つといえる。

#### (5) 結果と解釈

多モーダル統合は専門性判定で最大93%の精度に達し、単一モダリティの86%を上回った。

#### (6) 議論・結論

期待通りの側面は、画面ベース問題解決で多モーダルが単一モダリティより頑健なこと。足りない側面は、対象がチェスであり、ナレッジワーカーの日常作業やEEG中心の認知負荷定義ではない点。

### 7. Hamed, Rebello, and Munsell 2026: Relating Visual Attention and Learning in an Online Instructional Physics Module

URL: https://arxiv.org/abs/2602.08247  
Venue: PERC conference 2023 / arXiv 2026  

#### (1) 解こうとしている問題

オンライン教材を学習する学生が、画面を見ているか、学習内容について考えているか、マインドワンダリングしているかを、複数データから記録できるか。

#### (2) 既存方法の限界とアプローチ

オンライン学習では、ログだけでは画面を見ているだけなのか、内容を考えているのか、別のことを考えているのかわからない。Hamed, Rebello, and Munsell (2026) は、eye tracker、webcam、一人称グラス、画面録画、マウス/キーボードイベントを統合した。

#### (3) 実験/解析方法のポイント

物理大学院生が、Newtonの第二法則に関するオンライン教材を学習した。顕在的注意が学習環境に向いているか、学習内容について思考しているかを記録した。

#### (4) 解析方法だと何がわかるか

on-screen / off-screen と on-task / off-task を分けることで、「画面を見ているが内容を考えていない」「画面外だが学習内容を考えている」などを区別できる。

#### (5) 結果と解釈

多くの時間は on-task かつ on-screen だったが、マインドワンダリングの証拠も検出された。学習後テストの効率は改善し、on-screen/on-task時間と改善量には正だが統計的に有意でない相関があった。

#### (6) 議論・結論

期待通りの側面は、画面録画と操作イベントを含む多モーダルで注意状態を細かくラベル化できる点。足りない側面は、サンプルや課題が限定的で、EEGは含まれない点。

### 8. Altuwairqi et al. 2021: Student Behavior Analysis to Measure Engagement Levels in Online Learning Environments

URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8119613/  
DOI: https://doi.org/10.1007/s11760-021-01869-7  
Journal: Signal, Image and Video Processing, 2021  

#### (1) 解こうとしている問題

オンライン学習中の学生エンゲージメントを、顔表情、マウス、キーボードからリアルタイムに推定できるか。

#### (2) 既存方法の限界とアプローチ

顔表情のみ、またはマウスのみでは、エンゲージメントを安定して推定しにくい。Altuwairqi, Jarraya, Allinjawi, and Hammami (2021) は、表情、マウス、キーボードの3モダリティを組み合わせた。

#### (3) 実験/解析方法のポイント

42名のボランティアが書き込み課題を行い、顔表情、マウス移動、キーストロークを記録した。複数のデータセット/シナリオで、単一・二重・三重モダリティを比較した。

#### (4) 解析方法だと何がわかるか

単一/二重/三重モダリティの分類精度とMSEを比較し、三重モダリティが最も高精度なら、行動と顔表情の補完性が示される。

#### (5) 結果と解釈

多モーダルでは最高95.23%の精度、MSE 0.04が報告され、既存手法を上回った。

#### (6) 議論・結論

期待通りの側面は、顔・マウス・キーボードの統合によりエンゲージメント推定が改善する点。足りない側面は、EEGを含まず、エンゲージメントのラベルが集中/フロー/認知負荷と同一ではない点。

### 9. Xue et al. 2024/2025: Enhancing Online Learning: A Multimodal Approach for Cognitive Load Assessment

URL: https://www.tandfonline.com/doi/full/10.1080/10447318.2024.2327198  
Journal: International Journal of Human-Computer Interaction, online 2024 / volume 2025  

#### (1) 解こうとしている問題

オンライン学習中の認知負荷を、EEG、eye tracking、顔データの3モダリティから評価し、適応的なオンライン学習へ使えるか。

#### (2) 既存方法の限界とアプローチ

単一の生理信号や行動ログだけでは、オンライン学習の認知負荷を安定して測りにくい。Xue et al. は、EEG、視線、facial action recognition を統合して認知負荷評価フレームワークを構成した。

#### (3) 実験/解析方法のポイント

オンライン学習を対象に、3種類のモーダルデータを取得し、認知負荷評価モデルを検証した。公開ページでは、モデル精度91.52%が報告されている。

#### (4) 解析方法だと何がわかるか

分類モデルが認知負荷ラベルを高精度で当てるなら、複数モダリティを同期した特徴量が負荷状態を表しているといえる。

#### (5) 結果と解釈

評価精度91.52%が報告され、多モーダル解析結果は学習資源開発やオンラインコース最適化の参照に使えるとされる。

#### (6) 議論・結論

期待通りの側面は、EEGを含む多モーダル認知負荷評価が適応的支援に接続できる点。足りない側面は、特定テーマの学習モデルに限定され、複雑な学習シナリオや研究規模の拡大が今後の課題とされている点。

### 10. Bhatti et al. 2024: CLARE: Cognitive Load Assessment in REaltime with Multimodal Data

URL: https://arxiv.org/abs/2404.17098  
Venue: arXiv 2024  

#### (1) 解こうとしている問題

リアルタイム認知負荷評価のために、ECG、EDA、EEG、視線を同期した公開データセットとベースラインを提供すること。

#### (2) 既存方法の限界とアプローチ

認知負荷推定では、公開データセット、リアルタイム自己報告、複数モダリティの同期が不足しがちである。Bhatti et al. (2024) は、MATB-II課題で複雑度を操作し、10秒ごとの自己報告を ground truth として使った。

#### (3) 実験/解析方法のポイント

24名の参加者が、MATB-II による9分セッションを4回行った。課題複雑度は1分単位で変化し、参加者は10秒ごとに認知負荷を自己報告した。ECG、EDA、EEG、Gaze tracking が記録された。

#### (4) 解析方法だと何がわかるか

10-fold と leave-one-subject-out (LOSO) の両方で評価するため、同一参加者内の推定と未知参加者への汎化を分けて見られる。10-foldではECG+EDA+GazeのCNN、LOSOではECG+EDA+EEGの深層モデルがよいと報告されている。

#### (5) 結果と解釈

モダリティの最適組み合わせは評価条件で変わる。これはNEDOにとって重要で、万能な1モダリティではなく、個人内評価か個人間汎化かで必要な信号が変わることを示す。

#### (6) 議論・結論

期待通りの側面は、認知負荷を多モーダル・時系列・リアルタイム自己報告で扱える点。足りない側面は、MATB-IIという統制課題であり、ナレッジワーカーの自由作業や画面意味理解は含まれない点。

### 11. Angkan et al. 2024: CL-Drive / Multimodal Brain-Computer Interface for In-Vehicle Driver Cognitive Load Measurement

URL: https://arxiv.org/abs/2304.04273  
Dataset: https://github.com/Prithila05/CL-Drive  
Journal: IEEE Transactions on Intelligent Transportation Systems, 2024  

#### (1) 解こうとしている問題

運転中の認知負荷を、EEG、ECG、EDA、視線から推定するためのデータセットとベースラインを作ること。

#### (2) 既存方法の限界とアプローチ

運転のような現実的で安全重要なタスクでは、単一信号や統制課題だけでは実用的な負荷推定に足りない。Angkan, Behinaein, Mahmud, Bhatti, Rodenburg, Hungler, and Etemad (2024) は、シミュレータで複雑度の異なる運転条件を設計し、多モーダル生理信号と視線を同期記録した。

#### (3) 実験/解析方法のポイント

公開リポジトリによれば、21名の参加者が没入型車両シミュレータで運転し、9段階の認知負荷条件を3分ずつ行った。10秒ごとの主観的認知負荷がラベルとして使われた。

#### (4) 解析方法だと何がわかるか

binary/ternary classification と 10-fold/LOSO により、負荷レベル分類と未知被験者汎化を評価する。認知負荷を短い時系列セグメントで推定する実装設計の参考になる。

#### (5) 結果と解釈

論文は複数の機械学習/深層学習ベースラインを提供する。NEDO的には、10秒単位の自己報告ラベルと多モーダル同期が、作業レポートの変化区間設計に近い。

#### (6) 議論・結論

期待通りの側面は、現実的操作タスクで多モーダル認知負荷データを作った点。足りない側面は、運転タスクであり、画面/操作ログの意味的解釈やナレッジワーカーの成果物評価とは異なる点。

### 12. Medeiros et al. 2024: EEG as a Potential Ground Truth for the Assessment of Cognitive State in Software Development Activities

URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0299108  
Journal: PLOS ONE, 2024  

#### (1) 解こうとしている問題

ソフトウェア開発中の認知状態評価において、fMRIのような重い計測を参照しながら、EEGをより実用的な ground truth / reference として使えるか。

#### (2) 既存方法の限界とアプローチ

fMRIは脳活動の参照として強いが、開発作業の実用的計測には侵襲性・コスト・姿勢制約が大きい。Medeiros, Simões, Castelhano, Abreu, Couceiro, Henriques, Castelo-Branco, Madeira, Teixeira, and de Carvalho (2024) は、EEG、ECG、EDA、eye tracking/pupillography、fMRI を同期し、EEG特徴がソフトウェア開発関連脳領域のBOLD信号と対応するかを調べた。

#### (3) 実験/解析方法のポイント

21名のC言語経験者が選抜された。49名の候補から、プログラミング経験とCスキルの質問で選別し、16名がintermediate、5名がexpertに分類された。各runには自然言語読解、単純なコード理解、コード検査/バグ検出が含まれ、条件間に30秒のベースラインが入る。

#### (4) 解析方法だと何がわかるか

EEG特徴量を hemodynamic response function と遅延を考慮して変換し、fMRIのBOLD信号、特にソフトウェア開発タスクで関連が報告される insula 領域とPearson相関を取る。FDR補正後に有意な相関があれば、そのEEG特徴がfMRI参照信号に対応する候補になる。

#### (5) 結果と解釈

EEG特徴の一部がinsula領域と有意に相関した。全参加者にまたがる頑健な特徴として Hjorth Activity、Total Power、F4/FC4/C4 付近、4秒程度のhemodynamic delay が重要とされる。Theta関連特徴もソフトウェア開発文脈で有望とされる。

#### (6) 議論・結論

期待通りの側面は、EEGをソフトウェア開発中の認知状態評価の参照信号として使える可能性。足りない側面は、参加者数が限られ、fMRI内の統制された姿勢・課題であり、実際の開発環境ではない点。NEDOでは「EEGだけで正解を作る」のではなく、「EEGを他モダリティ検証の参照軸にする」という書き方がよい。

## Additional Notes: 壁打ち記録に出た補助文献

### Girardi et al. 2020: Recognizing Developers' Emotions while Programming

URL: https://arxiv.org/abs/2001.09177  

この研究は、プログラミング中の開発者感情を、生体センサを用いて認識することを扱う。壁打ち記録の「Müller & Fritz に倣い，NeuroSky の EEG ヘッドセットと Empatica E4 でプログラミング中の生理信号を計測し感情を認識」という流れに対応する。問題は、開発者の負の感情が進捗低下や作業体験に影響するにもかかわらず、通常の作業ログからは感情そのものが観測できないことである。

NEDOへの使い方は、集中力・認知負荷を「作業量」だけでなく、感情・快不快・進捗感と分けて扱う必要がある、という背景づけである。足りない側面は、感情認識が主題であり、画面録画/VLMによる要因説明やタスク細分化までは扱わない点。

### Ishida and Uwano 2019: Time Series Analysis of Programmer's EEG for Debug State Classification

URL: https://pman.uwanolab.jp/pman3.cgi?DOWNLOAD=131  

この研究は、プログラマのEEG時系列から、コード理解・バグ判断タスクの成否やデバッグ状態を分類する方向の研究である。結果として、成功した参加者では時間経過に伴って alpha/beta 帯域のパワーが有意に増えることが示されている。

NEDOへの使い方は、作業の「結果」や「進捗」とEEG時系列の関係を扱う根拠である。ただし、この研究はデバッグ/コード理解課題に限定され、画面操作ログや自由なナレッジワーク全般を扱うものではない。

### Khan et al. 2025: Assessing Cognitive Load Using EEG and Eye-Tracking in 3-D Learning Environments: A Systematic Review

URL: https://www.mdpi.com/2414-4088/9/9/99  
Journal: Multimodal Technologies and Interaction, 2025  

このレビューは、3D/XR学習環境におけるEEGとeye-trackingによる認知負荷測定を横断的に整理している。2009年から2025年までを検索し、51件の研究を対象にしている。重要なのは、frontal theta、parietal alpha、theta/alpha ratio、fixation duration、pupil dilation などの指標が使われる一方で、結果はタスク依存で、増加・減少・無差異が混在すると整理している点である。

NEDOへの使い方は、「EEG指標や視線指標は有望だが、単一の普遍的閾値で集中力変化を定義するのは危険」という根拠である。足りない側面は、対象が3D/XR学習であり、画面録画・操作ログ・ナレッジワークの成果物変化は中心ではない点。

### CLARE/CL-Drive と MAHNOB-HCI/DEAP の位置づけ

MAHNOB-HCI と DEAP は、EEG・顔動画・視線などを含む感情/affective computing 系の定番データセットとして参照できる。ただし、今回のNEDOで直接必要なのは「感情分類そのもの」ではなく、作業文脈に紐づいた集中・負荷・フローの定義である。そのため、これらは背景の基盤データとして扱い、主張の中心には Brown 2023、Kevic 2015、Fritz 2014、Müller and Fritz 2015、CLARE 2024、Medeiros 2024 を置くのがよい。

## NEDO向けの定義案

### Option 1: 変化点を生理信号で検出し、画面/操作ログで説明する

EEG/ECG/EDA/視線から認知負荷の時系列スコアを推定し、その変化点を画面/操作ログで説明する。

利点: 研究蓄積が厚い。CLARE/CL-Drive/Fritz系と接続しやすい。  
弱点: 画面/操作ログが後付け説明になり、作業速度や成果の情報がモデル本体に入りにくい。

### Option 2: 画面/操作ログで focused work 候補区間を作り、EEGで内的状態を弁別する

Brown et al. 2023 のようにログから focused work 候補を作り、その中で「順調な集中」「高負荷な停滞」「手は止まっているが思考中」「離脱」を EEG/生理信号で分ける。

利点: 「操作ログだけではflowを定義できない」という先行研究の限界を自然に超える。NEDOの課題設定に合う。  
弱点: 操作ログの取得範囲とプライバシー設計が重要になる。

### Option 3: 多モーダル潜在状態として集中・負荷・フローを定義する

EEG/生理信号、画面/操作ログ、成果物変化、自己報告を同時に使い、潜在状態として「集中/高負荷/フロー/停滞/離脱」を推定する。

利点: 単一閾値より的を射た定義になる。NEDOの新規性を最も強く出せる。  
弱点: データセット設計とラベル設計が難しい。

## Recommendation

提案書では Option 3 を目標として掲げ、最初の実証は Option 2 に落とすのがよい。

具体的には、次のように書ける。

> 本システムでは、集中力変化を EEG の単一周波数比の閾値超過として扱わない。操作ログから focused work 候補区間を抽出し、EEG/生理信号から内的負荷・注意・疲労の変化を推定し、画面録画/VLMからその区間の作業文脈と要因を説明する。これにより、手が止まっている区間を「考えている」「迷っている」「離脱している」に分け、逆に入力が多い区間を「順調に進んでいる」「高負荷で追われている」に分けることができる。

## Next Actions

- このメモをもとに、前回の `2026-06-05_system_problem_decomposition.md` から「雑誌会候補」色を薄め、NEDOの定義問題へ寄せて再構成する。
- 各論文を個別ファイルに分割するなら、優先度は Brown 2023、Kevic 2015、Fritz 2014、Müller and Fritz 2015、CLARE 2024、Medeiros 2024。
- 次の調査では、画面録画そのものをCV/VLMで自動アノテーションする研究を追加し、「文脈説明」の根拠を補強する。
