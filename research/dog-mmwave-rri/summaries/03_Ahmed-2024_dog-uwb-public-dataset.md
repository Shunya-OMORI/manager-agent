# UWB レーダと参照センサで記録したイヌのバイタルサイン公開データセット 詳細要約

> セクションは `rules/reading-paper.txt` の列順（書誌情報 →（a）〜（n）→ 本テーマ固有列（o）〜（q））．数値・主張には出典箇所を併記する．
> 本要約は，PubMed の書誌と PMC 版の全文（オープンアクセス）に基づく．
> **要確認**: 帯域通過フィルタの通過帯域について，本要約の作成時に得た抽出では呼吸帯 10--40，心拍帯 60--160 の単位が `Hz` と読めた．値域からは毎分（bpm，breaths/min）と解するのが自然であるため，本要約では bpm として記す．**原文 PDF で単位を直接確認すること．**
> **本論文はデータ記述論文（Data Descriptor）であり，仮説検証型の原著論文ではない．** そのため（c）（h）（j）などは，通常の原著論文とは性質が異なる．

## 書誌情報

- 原題: A public dataset of dogs vital signs recorded with ultra wideband radar and reference sensors
- 和訳タイトル: 超広帯域レーダと参照センサで記録したイヌのバイタルサインの公開データセット
- 著者（全員）: Shahzad Ahmed，Seongkwon Yoon，Sung Ho Cho（Ahmed と Yoon は同等に寄与）
- 所属機関: 漢陽大学校 電子工学科（Department of Electronic Engineering, Hanyang University, Seoul 04763, South Korea）… 著者全員
- 著名な著者: 原文に人物紹介の記載なし．
- 掲載誌: Scientific Data，11巻1号，論文番号 107
- 掲載誌の分野: データ記述（Data Descriptor）．Nature Portfolio の研究データ専門誌
- URL（必須）: https://doi.org/10.1038/s41597-024-02947-4 ／ https://pmc.ncbi.nlm.nih.gov/articles/PMC10803748/
- PMID: 38253685 ／ DOI: 10.1038/s41597-024-02947-4 ／ PMCID: PMC10803748
- 公開日: 2024年1月22日
- 本文アクセス: オープンアクセス
- データ公開先: Figshare，DOI: 10.6084/m9.figshare.23820915.v1
- 助成: 韓国国家研究財団（National Research Foundation of Korea, Grant: 2022R1A2C2008783）
- 主題語（Subject terms）: Biomedical engineering，Rehabilitation
- MeSH: Animals，Dogs/physiology，Heart Rate，Movement，Radar，Respiration，Vital Signs
- 分類フラグ:
  - 対象がイヌか: **はい**（麻酔下10頭，覚醒下20頭）
  - 目的が RR Interval か: **いいえ**（1 FPS へ平均化した心拍数・呼吸数のみ）
  - 原著論文か: **データ記述論文（Data Descriptor）**
  - 解析 or 介入: **解析研究**（データセット構築と技術的検証）

## 一文要約

本論文は，**UWB レーダに基づくイヌのバイタルサインとしては初となる公開データセット**を記述したものであり，手術室で全身麻酔下にあるイヌ10頭を臨床用参照センサと同期して 3 分間ずつ記録した場面と，集中治療室内で拘束せず自由に動くイヌ20頭を動画を参照として 30 分間ずつ記録した場面の二つからなる．技術的検証では，麻酔下の場面においてレーダと臨床センサの級内相関係数が心拍数 0.930，呼吸数 0.902 であった（Abstract；Technical Validation）．

## 用語集

- **超広帯域（ultra-wideband; UWB）レーダ**，**インパルス無線 UWB（impulse radio UWB; IR-UWB）**: 短パルスを用いる広帯域方式（Background & Summary）．
- **バイタルサイン（vital signs; VS）**: 本データセットでは呼吸数（breathing rate; BR）と心拍数（heart rate; HR）を指す（Background & Summary）．
- **級内相関係数（interclass correlation coefficient; ICCR）**: 二つの機器間の一致度を表す指標．0.7 を超えれば高い相関とみなされる（Technical Validation）．
- **ループバック再帰フィルタ（loop-back recursive filter）**: 静止クラッタを抑圧するフィルタ（Methods）．

## （a）研究の目的・研究課題

UWB レーダで記録したイヌのバイタルサインの公開データセットを構築し，臨床用参照センサとの同期記録によって技術的に検証したうえで公開すること（Abstract；Background & Summary）．

## （b）背景

イヌは家族の一員としてますます重視されているが，イヌは自らの体調を容易に表現できないため，その健康を監視することは難しい．呼吸数と心拍数は健康の主要な指標である（Background & Summary）．しかし，レーダによるヒトのバイタルサイン研究が広範に行われているのに対し，「レーダに基づくイヌのバイタルサインおよび関連する活動のデータセットは依然として不足している（radar-based dogs VS and related activity datasets are still lacking）」（Background & Summary）．

## （c）その論文が解こうとしている問題

参照センサと同期した，イヌ固有のレーダバイタルサインデータが公開されていないという欠落を埋めること（Background & Summary）．

## （d）既存の方法では解けない点 / アプローチの優位性（先行研究との比較）

著者はレーダによる動物計測の系譜を Lin（1975）のマイクロ波によるイヌの呼吸計測から説き起こす．より近年の研究として次を引用する（Background & Summary）．

Wang ら（2020）は UWB レーダによるイヌとネコのバイタルサイン計測を実証した（本要約 [02_Wang-2020](02_Wang-2020_dog-cat-uwb-vital-signs.md) と同一論文である）．Wang ら（2019）は IR-UWB レーダを用いたバイタルサイン計測においてヒトと動物を弁別した．Ma ら（2019）は壁越し条件下で静止したヒトとイヌの目標を識別した．

ヒトのバイタルサインについては，Shi ら，Schellenberger ら，および小児のデータなど，複数の公開レーダデータセットが既に存在する．しかし著者は，**ヒトとイヌからバイタルサインを抽出することは実質的に異なる**と主張する（Background & Summary）．

本論文は「史上初の超広帯域レーダに基づくイヌのバイタルサイン（UWB-DVS）データセット（the first ever ultra wideband radar-based dog vital sign (UWB-DVS) dataset）」であることを新規性として主張する（Background & Summary）．

## （e）対象（サンプル/参加者）

**場面1（麻酔下）**: イヌ**10頭**，4〜12歳，体重 2.9〜12.0 kg．犬種はダックスフント，柴犬，プードル（4頭），シュナウザー，マルチーズ，ポメラニアン，ポンピッツ．いずれも手術のため入院しており，術式は椎間板手術，乳び胸，乳腺腫瘍，靱帯断裂，胆嚢摘出，去勢・避妊，子宮蓄膿症，抜歯であった（Methods）．

**場面2（覚醒下）**: イヌ**20頭**，4〜12歳，体重 7.2〜16.1 kg．犬種はシーズー，マルチーズ（7頭），雑種（3頭），ポメラニアン（2頭），ハウンド，ウェルシュ・コーギー，プードル，ダックスフント，柴犬．いずれも手術のため入院していた（Methods）．

## （f）実験/解析方法のポイント（対象・データ・除外条件）

レーダは Xethru-X4 IR-UWB レーダ（Novelda, Norway）である．中心周波数 **8.75 GHz**，帯域幅 1.50 GHz（−10 dB），フレームレート 50 フレーム/秒，サンプリング周波数 23.32 GHz，パルス繰返し間隔 40.50 MHz，送受信は1対の構成である．被験体からの距離は **0.3 m** である（Methods）．

**場面1**は手術室で行った．「麻酔下のイヌのデータを，レーダと臨床用参照センサを用いて収集する（Data from fainted dogs in the operating room are collected using radar and clinical reference sensors.）」．麻酔は，導入薬としてプロポフォールを併用した全身麻酔である．「全身麻酔と，追加の導入薬としてのプロポフォールを用いて，イヌに意識消失を導入した（General anesthesia along with Propofol as an additional induction agent, was used to induce unconsciousness in the dogs.）」．記録は 1 頭あたり **3 分間**であり，参照データ 180 標本，レーダデータ 9,000 標本（50 FPS）となる（Methods）．

**場面2**は集中治療室で行った．「イヌは集中治療室（ICU）チャンバ内で拘束せずに保たれ，データを 30 分間取得する（The dog is kept unconstrained inside the Intensive Care Unit (ICU) chamber and data are captured for 30 minutes.）」．レーダデータは 90,000 標本である（Methods）．

参照センサは場面ごとに異なる．**場面1**は「Bionet Co., Ltd. 製の BM7Vet Pro 心電図センサ（A BM7Vet Pro ECG sensor, manufactured by Bionet Co., Ltd）」であり，「臨床的に承認された獣医用バイタルサイン監視センサ（a clinically approved veterinary vital signs monitoring sensor）」である．心電図電極を介して **1 FPS** で標本化し，心拍数と呼吸数を与える．**場面2は臨床センサを用いず，動画カメラのみ**である（Methods）．

データは CSV 形式で Figshare（DOI: 10.6084/m9.figshare.23820915.v1）に公開されており，MATLAB R2020 以降を要する `load.m` で読み込む（Data Records；Usage Notes）．

## （g）研究方法

データ記述（データセットの構築，技術的検証，公開）．

## （h）解析方法で何がわかるか（数理的・統計的な成功基準）

著者がレーダからバイタルサインを抽出するために適用した処理は次のとおりである（Methods）．直流成分の除去，静止クラッタ抑圧のためのループバック再帰フィルタ，イヌの位置を決めるための分散計算，周波数の定量化のための高速フーリエ変換（FFT），呼吸帯（10--40 bpm）と心拍帯（60--160 bpm）を分離する二つの帯域通過フィルタ，および連続監視のための滑動窓解析である．**拍の検出（beat detection）は行っていない．**

技術的検証は，散布図，Bland-Altman プロット，および級内相関係数（ICCR）による．「観察対象の二つの機器の間の高い相関を示すとみなされるのは 0.7 を超える値である．本件では ICCR 値は 0.9 を超えた（Any value above 0.7 is considered to indicate a high correlation between the two devices under observation. In our case, the ICCR value was above 0.9.）」（Technical Validation）．

## （i）結果・結論

場面1における級内相関係数は，呼吸数 **0.902**，心拍数 **0.930** である．平均絶対誤差は，呼吸数 **2.3 breaths/min**，心拍数 **3.7 beats/min** であった（Technical Validation）．

Abstract は「第一の場面では心拍数・呼吸数の計測についてレーダと臨床センサの間で 0.9 を超える相関係数が示された」と述べ，第二の場面はダッシュボードによりバイタルサインと動きのデータを提示し，「レーダセンサの長期監視能力を実証している（demonstrating the long-term monitoring capability of the radar sensor）」と述べる（Abstract）．

## （j）実験・解析結果とその解釈

麻酔下・距離 0.3 m・3 分間という条件では，UWB レーダは臨床承認済みの獣医用心電図センサに対して級内相関 0.9 超，心拍数の平均絶対誤差 3.7 beats/min を達成した．**ただしこの照合は 1 FPS へ平均化した値どうしの比較である**（Methods；Technical Validation）．

覚醒下・自由行動の場面2には臨床参照が存在せず，動画観察と動画に基づく呼吸の推定しか得られない．バイタルサインが信頼できるのは体動の少ない期間に限られる（Usage Notes；Technical Validation）．

## （k）研究上の示唆・意義

データセットは二つの異なる用途を可能にする．場面1（臨床参照センサ付きの麻酔下のイヌ）はアルゴリズムの検証と性能比較（ベンチマーク）を支える．場面2（覚醒し自由に動くイヌ）は長期監視の実現可能性と，健康上の異常を検出するための個体別の基準値の確立を実証する（Usage Notes）．

## （l）限界・課題

著者は次の限界を挙げている．場面2には臨床参照データがない．「場面2では，動くイヌの身体に装着する臨床センサが医療専門家により推奨されないため，臨床参照データが利用できないものの（Although the clinical reference data are not available in scenario 2 since clinical sensors worn on the bodies of moving dogs are not recommended by medical experts）」，カメラ観察と動画に基づく呼吸の推定のみが利用できる（Usage Notes）．また，バイタルサインが信頼できるのは体動の少ない期間に限られる．

## （m）筆者が捉える期待通りの側面と足りない側面

- 期待通り: イヌのレーダバイタルサインとして初の公開データセットを，臨床承認済みの獣医用センサとの同期のもとに構築し，級内相関 0.9 超を得た（Abstract；Technical Validation）．覚醒・自由行動下の 30 分記録を20頭分そろえた（Methods）．
- 足りない側面: 覚醒下の場面2に臨床参照がなく，動画のみである（Usage Notes）．麻酔下の場面1も参照・レーダともに 1 FPS の平均値であり，拍単位の情報が保存されていない（Methods）．

## （n）キーワード

Biomedical engineering，Rehabilitation（Subject terms）．著者キーワードの明示は原文に確認できず．

---

## （o）使用機材と実験条件

- レーダ: Xethru-X4 IR-UWB レーダ（Novelda, Norway）．**中心周波数 8.75 GHz**（ミリ波帯ではない），帯域幅 1.50 GHz（−10 dB），フレームレート 50 FPS，サンプリング周波数 23.32 GHz，パルス繰返し間隔 40.50 MHz，送受信1対（Methods）．
- 距離: **0.3 m**（Methods）．
- 個体: 場面1 が**10頭**（4〜12歳，2.9〜12.0 kg），場面2 が**20頭**（4〜12歳，7.2〜16.1 kg）．いずれも手術のため入院中（Methods）．
- 覚醒状態: 場面1 は**プロポフォール併用の全身麻酔下**，場面2 は**覚醒**（Methods）．
- 拘束: 場面2 は ICU チャンバ内で**非拘束・自由行動**（Methods）．
- 体動: 場面1 は麻酔下のためほぼなし．場面2 は**あり**（動画で参照）（Methods）．
- 記録長: 場面1 が 1 頭あたり **3 分**，場面2 が 1 頭あたり **30 分**（Methods）．

## （p）正解データと評価指標

- 参照センサ: 場面1 が **BM7Vet Pro 心電図センサ**（Bionet Co., Ltd.，臨床承認済みの獣医用バイタルサイン監視センサ），**1 FPS 標本化**．場面2 は**動画カメラのみで臨床参照なし**（Methods）．
- 参照値の粒度: **1 FPS へ平均化した心拍数・呼吸数**．原文は「レーダで抽出したバイタルサインは，参照センサのデータに合わせるため 1 FPS へ平均化された」と述べる（Methods）．
- 評価指標: 散布図，Bland-Altman プロット，級内相関係数（ICCR），平均絶対誤差（Technical Validation）．
- **RR Interval を取っているか**: **取っていない．** 信号処理は帯域通過フィルタと FFT による周波数の定量化であり，**拍の検出を行っていない**（Methods）．データセットにも R 波位置や拍間隔の注釈は含まれない．参照・レーダともに 1 FPS の平均値である．
- 精度水準: 麻酔下で ICCR 0.930（心拍数）・0.902（呼吸数），平均絶対誤差 3.7 beats/min・2.3 breaths/min（Technical Validation）．

## （q）本テーマへの含意

**位置づけ: 正解データ問題に対する最有力の外部資源だが，そのままでは本テーマに使えない．**

- **最大の価値は「イヌ30頭・臨床承認済み心電図センサ付き」という規模である．** 本テーマの未確定事項のうち「RR Interval の正解をどの接触センサで取るか」に対し，**BM7Vet Pro という臨床承認済みの獣医用心電図センサ**という具体的な答えを与える．研究室で機材を選ぶ際の第一候補になる．
- **しかし，このデータセットで RR Interval の研究はできない．** 理由は三つある．第一に，**レーダが UWB（中心 8.75 GHz）でありミリ波ではない**．第二に，**参照もレーダも 1 FPS へ平均化されており，拍単位の情報が原理的に失われている**．第三に，拍単位の正解が取れている場面1 は**全身麻酔下**であり，[02_Wang-2020](02_Wang-2020_dog-cat-uwb-vital-signs.md) と同じく，本テーマが対象としたい自律神経由来の拍間隔変動が消えている条件である．
- **場面2 が示す構造的な困難**: 覚醒・自由行動のイヌ20頭を 30 分記録しながら，**臨床参照が一つも取れていない**．理由は技術的制約ではなく，「動くイヌの身体に装着する臨床センサは医療専門家により推奨されない」という**運用上・倫理上の制約**である．**これは本テーマにとって重い警告である．** 覚醒下のイヌで拍単位の正解を取るには，この制約を回避する手段（[01_Bowden-2024](01_Bowden-2024_canine-mmwave-hr-depth-camera.md) が用いた Polar H10 のような非侵襲の胸部ベルト，または獣医の管理下での短時間記録）を設計段階で用意する必要がある．
- **「初」の主張の範囲**: 著者は「史上初の UWB レーダに基づくイヌのバイタルサインデータセット」を主張する．**ミリ波帯ではないため，「ミリ波によるイヌのデータセット」は依然として空白である．** 本テーマがデータを自前で取る場合，その副産物としてのデータセット公開自体が貢献になりうる．
- **帯域設定の参考値**: 著者は心拍帯を **60--160 bpm** として帯域通過フィルタを設計した（要単位確認）．これはイヌの心拍数域の実務的な想定として使える．ただし**帯域通過フィルタで 60--160 bpm を切り出す設計は，平均心拍数を得るには十分でも RR Interval には不適である．** イヌの呼吸性洞性不整脈は平均心拍の 40.1%±4.5% に達するとされ，瞬時心拍がこの帯域内を大きく揺れ動くため，狭帯域のフィルタは**変動そのものを削り落とす**．本テーマは，周波数領域の帯域通過ではなく時間領域の拍検出を採る必要がある．
