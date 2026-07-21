# リアルタイム脳電気活動モニタリングのためのEEG眼鏡

- 原題: EEG glasses for real-time brain electrical activity monitoring
- 著者: Renato Zanetti, Amir Aminifar, David Atienza
- 掲載誌: Scientific Reports, Vol. 15, Article 43574, 2025
- DOI: https://doi.org/10.1038/s41598-025-29893-4
- 公開日: 2025年11月29日

> 本文、表、図キャプション、結論、付記を全文和訳した。数値、式番号、
> 引用番号、固有名詞は原文に合わせた。参考文献は書誌情報の誤変換を
> 避けるため原題を保持した。横長のTable 4はPDFとレイアウト抽出版を
> 参照して解釈した。

## 要旨

ウェアラブルデバイスは、個別化された長期健康モニタリングの基盤となりつつあり、早期介入とデータに基づく医療判断を可能にする。本研究は、目立たないリアルタイム脳波（electroencephalography; EEG）モニタリングを可能にする最先端スマートウェアラブルデバイス、e-Glassを提示する。評価の結果、e-Glassは臨床EEG記録に関する国際的ガイドラインを満たした。また、取得データは研究用EEG装置Biopacによる記録に対してPearson相関係数0.93を示した。

提案したEEG取得デバイスの概念を、てんかん発作検出と認知負荷モニタリング（cognitive workload monitoring; CWM）の二つの応用で評価した。まず、e-Glass専用に設計した軽量エッジ機械学習方式を提示した。CHB-MITデータセットのEEG 982.9時間で評価した結果、全体感度64%、24名中11名で感度100%、1日当たり2.35件の誤警報を達成した。同様に、e-GlassによるCWM方式は未知データで正解率74.5%を達成した。これらの結果は、e-Glassが外来環境において、てんかん発作だけでなく利用者の認知状態も、目立たずリアルタイムに監視できる可能性を示す。

## はじめに

国際連合は、2050年までに世界の6人に1人が65歳以上となり、その多くが低・中所得国で生活すると予測している [1]。人口高齢化に伴って各国の医療制度への負担が増すため、病院中心の治療構造にかかる費用を抑えるスマートな解決策が必要になる。ウェアラブルデバイスは、継続的かつ個別化された臨床データを提供し、早期介入とデータに基づく医療判断を可能にすると期待される [2]。エッジ機械学習（edge-ML）とInternet of Things（IoT）を利用するウェアラブルは、てんかん発作検出など、健康状態をリアルタイムに監視・検出・予測するための基盤となる [3]--[8]。

てんかんは反復性発作を特徴とする脳疾患であり、人口1,000人当たり4--8人にみられ、世界で4番目に多い神経疾患である [9]。ウェアラブルによるてんかん監視は、発作をリアルタイムに追跡して患者と介護者へ通知する患者管理手段であり、てんかんにおける予期せぬ突然死（SUDEP）などを防ぐ可能性がある [10]。てんかん患者（People With Epilepsy; PWE）が現在選択できる検証済み製品には、Epi-Care、Empatica、Nightwatchがある [11]。これらは強い体動を伴う全般強直間代発作（GTCS）を対象とし、加速度計または少数の末梢生体信号だけでも妥当な性能を得られる。しかし、GTCSはPWEが経験する全発作の15%未満である [12]。他の発作型を扱うには、PWEの診断と監視における標準であるEEGが必要になる [12]。

既存の市販無線EEG取得装置は一般に大きく目立ち、PWEに受け入れられにくい [13]。ウェアラブルEEGの開発には複数の課題がある。第一に、差別を避けるには目立たない形状が必要である [14]。第二に、採用と長期使用を促すには、低い誤警報率（false-alarm rate; FAR）と高い感度が必要である [11]。被験者監視の最新アルゴリズムは多くのEEGチャネル、最低でも18チャネルに依存するが、ウェアラブルEEGではそれだけのチャネルを使用できない [7], [15], [16]。少数チャネルを補うには専用の複雑な機械学習が必要になる一方、携帯性、装着性、快適性、目立ちにくさを確保するため、対象端末のメモリ、処理能力、電池容量は制限される。

著者らは先行研究において、スマート眼鏡へ収まる前頭側頭部4電極だけによるてんかん発作検出を先駆的に検討した [4], [17], [18]。AttentivUも眼鏡形状を採用し、TP9とTP10間の1双極EEGチャネルから注意と関与に関するフィードバックを生成する [19], [20]。Leeら [21] はEEGとEOGを組み合わせたウェアラブル医療・HMI用スマート眼鏡を提示した。さらにGAPses [22] は、RISC-VプロセッサGAP9上でEEGとEOGを処理し、SSVEP、運動分類、EEGバイオメトリクスを扱う。これらの基盤は多用途だが、てんかん発作検出を直接の対象としていない。

本研究は、てんかんを対象としたリアルタイムEEG監視用スマートウェアラブルシステムe-Glassを提示する。Fig. 1(a)の設計は、社会的スティグマと差別へ対処するため、目立たず妨げにならないウェアラブルEEGを意図している。少数EEG電極と、資源制約端末向けに最適化した機械学習処理によって、高性能な発作検出を目指す [4], [7], [17]。リアルタイムEEG処理はCWMにも使用できる [23]。

本研究の主な貢献は次の通りである。

1. PWEの個別監視を目的とし、目立たないEEG取得とリアルタイム処理を行うウェアラブル基盤e-Glassを提示する。計算、メモリ、エネルギーの制約へ合わせた軽量edge-ML方式も提示する。
2. e-Glassハードウェアの電気的特性とEEG取得能力を評価する。入力換算雑音（input-referred noise; IRN）は最小`0.16 µV RMS`、noise-free bits（NFB）は18.41 bitで、International Federation of Clinical Neurophysiology（IFCN）の臨床EEGデジタル記録ガイドライン [24] に適合した。研究用装置との平均Pearson相関は最大0.93であり、帯域パワーとalpha波同期も類似した。
3. 資源制約端末向けの機械学習発作検出処理を提示する。CHB-MITの982.9時間を用い、F7T7とF8T8の2双極チャネルだけで全体感度64%、24名中11名で感度100%、FAR 2.35件/日を得た。225 mAh電池1回の充電で最大28.5時間動作する。
4. ウェアラブルCWMの機械学習設計法と処理戦略を実験データで評価し、未知データで正解率74.5%、感度と特異度の幾何平均74.0%を得た。

**Fig. 1. 提案e-Glassシステム。** (a) 1: メイン基板、2: 電極スナップコネクタ、3: 電池ケース、4: バイアス電極。(b) メイン基板のハードウェアブロック図。(c) e-GlassのRTOSが使用する4主要スレッドを示すファームウェア状態図。(d) e-Glass内のデータフローと処理を表すedge-ML方式。

## e-Glass

e-Glassは、広く受け入れられているウェアラブル形状である通常の眼鏡を基礎とし、目立たないリアルタイム脳電気活動、すなわちEEG監視を可能にする。日用品へ機能を組み込むことで、大型市販EEG装置に伴う社会的スティグマと差別の軽減を目指す [13], [14]。Fig. 1はシステム、ハードウェア、ファームウェア、端末上のリアルタイム機械学習処理を示す。

### e-Glassのシステムとハードウェア構成

通常の眼鏡に近い外観を保つため、ハードウェアをテンプル部へ埋め込んだ。システムは、信号取得、データ処理、通信、オンボードメモリの4サブシステムからなる。各部品には、単独動作と必要時の割込み生成が可能な低消費電力部品を優先した。

e-GlassはADS1299アナログフロントエンド [25] に基づき、基準電極方式の4 EEGチャネルを備える。10--20国際電極配置法 [20] のF7、T7、F8、T8を使用し、基準電極を左乳様突起上へ配置する。さらに、身体の一点を電源範囲内の電位へ駆動するアクティブバイアス電極を備え、同相信号除去比（common-mode rejection ratio; CMRR）を高める。バイアス回路によるCMRR利得は少なくとも13 dBである [26]。

電極にはsoft-dry電極を使用する。導電性ゲルと大がかりな皮膚前処理が不要なため外来環境に適する一方、電極間インピーダンスの不一致による雑音を受けやすい。そこで、各電極近傍へ電圧フォロワを置き、アクティブ電極を構成した [27]。回路から見た入力インピーダンスを高め、皮膚・電極界面と回路入力の分圧を抑える。電極位置で電流増幅を行うことは信号強度を高め、配線インピーダンスを下げ、容量結合雑音も軽減する。

### e-Glassのファームウェア構成

ファームウェアはARM CMSIS-RTOS [28] 上に構築し、STMicroelectronicsのlow-level driverとhardware abstraction layer [29] を使用する。RTOSにより、予測可能な実行時間と資源アクセス、イベント駆動による応答性、タスク並列化、メモリ管理と自己監視用APIを得る。

Fig. 1(c)のイベント駆動構成では、queue、mail queue、semaphoreによってデータ転送とタスク実行を同期する。外部イベントはinterrupt service routine（ISR）で処理する。主要タスクは次の4個である。

- `SysMgnt`: ボタン、電池、システム状態などの基本機能を監視・制御する。
- `DataMgmt`: BLE通信、EEG、加速度など、データ関連イベントを管理する。
- `DataProc`: 利用者監視のためのリアルタイム処理を実行する。
- `Idle`: 他に実行可能なタスクがないときCPUを使用する既定タスクである。

共有資源は`HPmail`、`LPmail`、`LPsemaphEvt`で同期する。たとえば`DataMgmt`は、BLEまたはEEGフロントエンドのISRから`HPmail`を受け取るまで待機する。データ損失と通信失敗を避けるため、`DataMgmt`へ最高優先度を割り当てる。リアルタイム処理では`DataMgmt`が`DataProc`へ`LPmail`を送り、コンテキストスイッチを起こす。全タスクが待機すると`Idle`が動き、tickless動作によって周期tick割込みを止める。復帰時にはRTCの値からRTOS tick数を補正する。

平均電流を減らすため、Cortex-M4の低電力モードを利用する。処理時は80 MHzで高速に実行し、タスクが待機すると他のタスクへ切り替え、すべて待機中なら低電力モードへ入る。未使用周辺回路のclock gatingも行う。EEGと加速度センサの割込みで取得データを循環バッファへ格納し、バッチがそろうと`DataMgmt`へ通知する。

### e-Glassのedge-ML

長期の外来リアルタイム監視では、ウェアラブル端末のメモリ、演算能力、電池容量が制約となる。一方、現代のマイクロコントローラはSIMD、アクセラレータ、大容量RAM・Flash、超低電力モードを備え、専用DSP処理を実行できる。通信より計算の消費電力が低いことから、エッジ処理と組込み機械学習は電池寿命の改善に寄与する [23], [31], [32]。

e-GlassではARM向けに最適化されたCMSIS-DSP [28] と、クロスコンパイルしたGNU Scientific Library（GSL）を用いる。処理ブロックは次の通りである。

- 前処理: 標本単位の平均除去、IIRバンドパスフィルタ、少数チャネル向け軽量アーチファクト除去 [23]、GSLの離散wavelet変換。
- 特徴抽出: line length、平均振幅、平均、分散、標準偏差、Hjorthパラメータ [33], [34]、EEG帯域別パワー [15]、Shannon、Tsallis、Rényi、Sample、Permutation entropy [35]。
- 推論: 高い精度と過学習への頑健性を持つRandom Forest（RF）[36]。

各ブロックは精度とエネルギー予算に応じて単独または組み合わせて使用できる。基本的なe-Glass応用では、少なくともフィルタ、特徴抽出、状態推論モデルを用いる。

## 結果と考察

最初に、IFCNの臨床EEGデジタル記録ガイドライン [24] と比較してIRNなどの電気的特性を評価した。次に、市販研究用装置Biopac BN-EEG2と比較してEEG取得能力を評価した。最後に、発作検出とCWMの結果を示した。

### e-Glassハードウェアの電気的特性

回路雑音は、EEGのような低SNR用途でADC性能を低下させる。ADS1299のデータシートは、標本化周波数と入力利得ごとにIRN、dynamic range（DR）、NFB、effective number of bits（ENOB）を示す。IFCNガイドラインは、(1) 標本化周波数200 sample/s以上、(2) 分解能0.5 µV以下、(3) 入力インピーダンス100 MΩ以上、(4) 増幅器入力で各チャネルのCMRR 110 dB以上、(5) 0.5--100 Hzの任意周波数でIRN 1.5 µV peak-to-peak未満を求める [24]。

**Table 1. IFCNガイドラインとの比較。**

| 項目 | IFCNガイドライン | e-Glass |
| --- | ---: | ---: |
| 標本化周波数 | ≥ 200 Hz | 250 Hz |
| 分解能 | ≤ 0.5 µV/bit | 0.023 µV/bit |
| 入力インピーダンス | ≥ 100 MΩ | > 1,000 MΩ |
| CMRR | ≥ 110 dB | 110 dB（ADS1299入力） |
| IRN（0.5--100 Hz） | ≤ 1.5 µV peak-to-peak | 1.07 µV peak-to-peak |

ADS1299を用いたe-GlassはIFCN条件を満たす。ADS1299の最低標本化周波数は要求値を上回り、その設定で取得雑音が最小となる。入力電圧フォロワの最大入力バイアス電流は1 pAであるため、入力インピーダンスは1 GΩを上回ると見込まれる。delta-sigma ADCのoversamplingとfilteringにより、評価周波数50 HzのIRNもIFCN上限を大きく下回った。

ADS1299は増幅器入力で110 dB以上のCMRRを保証する。著者らが電極スナップコネクタで測ったopen-loop CMRRは、入力保護回路とフィルタによる劣化を含め89.1 dBであった。BIAS回路が少なくとも13 dB改善するため、システム全体では102 dB以上と見積もられる。対象帯域が30 Hz以下であることを考えれば十分と著者らは判断した。ただし、これはIFCNの110 dBという増幅器入力での値とは測定点が異なる。

**Table 2. 静的雑音測定とADC性能。** PGA 24 V/V、標本化周波数250 Hz、帯域0.5--65 Hz。

| 対象 | IRN RMS | IRN peak-to-peak | NFB | ENOB | DR |
| --- | ---: | ---: | ---: | ---: | ---: |
| e-Glass | 0.16 µV | 1.07 µV | 18.41 bit | 19.64 bit | 118.24 dB |
| ADS1299データシート | 0.14 µV | 0.98 µV | 18.54 bit | 19.85 bit | 119.5 dB |

データシート値は複数評価基板の平均であり、外部入力回路のJohnson--Nyquist雑音などを含まない。e-Glassは電極コネクタ入力から測定し、外部回路を含む。IRNがわずかに高いだけであることは、著者らによればハードウェア設計の品質を示す。

### EEG取得能力の評価

ベンチ試験に加え、e-Glassと研究用Biopac BN-EEG2 [37]--[39] を比較した。Fig. 2は被験者12で両装置から同時取得したEEGを示し、閉眼後に約10 Hzの明瞭なalpha波同期が現れた。これは脳活動を取得できた指標である [40]。

**Fig. 2.** F7電極においてe-GlassとBN-EEG2の両方で観察された、閉眼中のalpha帯域同期。

Session 1、Task 1の閉眼区間から自発EEGのpower spectral density（PSD）を求めた。Fig. 3では、多くの被験者で8--12 Hzのalpha帯域同期が観察され、e-GlassとBN-EEG2のPSDは視覚的に強く対応した。一部ではe-Glassの0.5--3 Hzエネルギーが大きかった。著者らは、乾式電極に一般的な皮膚・電極インピーダンス不一致が原因と考えた [41]。

**Fig. 3.** 被験者が閉眼している間にF7から取得したEEGのWelch periodogram。青線がe-GlassのPSD。

Bland--Altman図 [42] では、全被験者で測定間の平均biasが小さく、大半のPSD差が95%区間内に入った。

**Fig. 4.** F7で取得したe-GlassとBiopac BN-EEG2のPSDについて、両者の平均に対してe-GlassからBiopacを引いた差を示すBland--Altman図。MDは平均差、SDは標準偏差。

標本化周波数差を補正するためDynamic Time Warping（DTW）を適用し、1分間のEEGからPearson相関を求めた。大半の被験者で高い相関を示し、開眼中F7の平均は`0.93 ± 0.06`であった。被験者10の閉眼F7だけ相関が0.30と低く、目視確認では高振幅の瞬目アーチファクトが原因であった。

**Table 3. e-GlassとBiopac信号間のPearson相関。**

| 条件 | F7 平均 ± SD | T7 平均 ± SD |
| --- | ---: | ---: |
| 開眼 | 0.93 ± 0.06 | 0.88 ± 0.08 |
| 閉眼 | 0.88 ± 0.18 | 0.88 ± 0.09 |

### 応用結果

Time-Slice Cross-Validation（TSCV）による発作検出では、18チャネルfull-capが試験対象132発作中99件を検出し、平均感度80%となった。しかし、EEG capはスティグマのためPWEに受け入れられにくい。e-Glassの2双極チャネルに限定すると、前頭側頭部に発作活動がないCHB17、CHB21などが含まれるため、感度は64%へ低下した。それでも11名で感度100%を得た。

e-Glassとfull-capのFARは、それぞれ2.35件/日と1.81件/日であり、装着型装置の目標とされる1件/日に近かった [43]。Ingolfssonら [44] は発作とアーチファクトを組み合わせ、平均感度65.27%を得たが、最大24件/日の誤警報があった。e-Glassは感度が近く、FARは低かった。18チャネル以上の畳み込みネットワーク [16] と比べても、e-GlassのF1 59%、感度64%は、同研究のF1 59%、感度58.3%に近く、FARは同研究の0.5件/時、すなわち12件/日より低かった。

**Table 4. 発作検出性能。**

| 構成 | 平均感度 | 平均precision | 平均F1 | FAR |
| --- | ---: | ---: | ---: | ---: |
| e-Glass（F7T7、F8T8） | 0.64 | 0.65 | 0.59 | 2.35件/日 |
| Full-cap（18チャネル） | 0.80 | 0.75 | 0.73 | 1.80件/日 |

Table 4は各被験者の発作数、試験発作数、感度、precision、F1、FARも掲載する。全体では24名、185発作のうち132発作を試験した。

CWMでも、4単極チャネルのe-Glassは19チャネルfull-capより試験Gmeanが6.2ポイント低いだけであった。RF最適化によりFlash要求量はfull-capの5.7分の1となった。Jaoら [45] は同じデータセットをfull-capで分類して正解率77%、Dell'Agnolaら [46] は4末梢生体信号を用いて80.2%を報告した。e-Glassは少数EEGチャネルだけで近い性能を得た。

**Table 5. CWM性能。**

| 構成 | CV Accuracy | CV Gmean | 試験Sensitivity | 試験Specificity | 試験Accuracy | 試験Gmean | モデル容量 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| e-Glass | 75.8 ± 4.7% | 75.1 ± 5.0% | 82.9% | 66.1% | 74.5% | 74.0% | 113.5 KB |
| Full-cap | 82.0 ± 5.2% | 81.3 ± 5.8% | 73.3% | 87.7% | 80.5% | 80.2% | 645.7 KB |

e-Glassは18特徴、200本の木、full-capは33特徴、400本の木を使用した。edge-ML処理時間は発作検出1推論当たり26.45 ms、CWM 1推論当たり56.4 msであった。CPUは最大97%の時間idleとなり、平均電流を約7.8 mAへ抑えた。ADS1299は常時動作で約4.6 mAを消費する。225 mAh電池で最大28.5時間動作する。RAM使用量は発作検出4,774 byte、CWMはアーチファクト除去用信号を保持するため8,256 byteであった。

## 方法

頭部サイズへ合わせられる可変3D設計に基づき、e-Glass試作機を開発した。電極保持部にはばね入りpiston機構を設け、皮膚への圧力を高め、小さな振動を減衰させてEEGのSNRを改善した。電気的特性評価と、Biopacとの同時・近接位置計測によるEEG取得評価を行った。さらに、二つの想定応用と機械学習評価法を定めた。

**Fig. 5. e-Glass試作機。** (a) piston型電極保持部とDätwyler製SoftPulse soft-dry電極を備えた試作機。(b) 実験時の電極位置。

### e-Glass試作機のハードウェア設計

3D設計には、(1) 取得・処理・通信用メイン基板、(2) アクティブ電極とpiston型保持部を含む4 EEGチャネル、(3) Li-ion電池ケース、(4) バイアス電極、(5) 基準電極、(6) piston型保持部とSoftPulse電極を含む。

基板は市販の工業用部品で構成した。ADS1299により最大22 nV/bitの分解能と`< 1 µV RMS`のIRNを持つ小型EEGフロントエンドを構成し、4チャネル同時取得時のactive消費電力は22 mW、4.6 mAである。処理にはSTM32L476を用いた。これはFlash 1 MB、RAM 128 KB、最大80 MHz、1.25 DMIPS/MHzの超低消費電力32-bit ARM Cortex-M4である。9個の電力モードとclock gatingを備え、RAMとRTCを保持するStop2では1.4 µAを消費する。

通信はSTMicroelectronics BlueNRG-MSによるBLEとUSB 2.0を使用する。BLEは専用アプリとのデータ交換、Internet接続、状態監視に使う。端末内でリアルタイム処理するため通常のthroughput要求は小さい。ストリーミング時は送信0 dBmで8.2 mA、sleep時は2.4 µAを消費する。データ記録用64 Mbit外部Flashは書込み時最大3.5 mAを消費する。

### 電気的特性評価

雑音性能を評価するため、ADS1299外部でEEGチャネルを短絡し、連続10,000標本以上を取得した（Fig. 6）。単電源のため、チャネル入力と基準を電源範囲内の既知電圧、すなわち電池から得た1.5 Vへ短絡した。取得標本の平均電力から式(1)によりIRNのRMSを求め、RMSへ6.625を掛けてpeak-to-peak値を推定した。

**Fig. 6. 入力換算雑音測定。** ADS1299より外側の回路を含めてIRNを測るため、外部入力を短絡した。

IRNからDR、NFB、ENOBを式(2)--(4)で計算した [47]。アクティブ電極の電圧フォロワ、入力保護、フィルタの雑音も測定へ含まれる。設定は最大入力利得24 V/V、最低標本化周波数250 Hzとした。

```math
IRN=\sqrt{\frac{\sum_{j=1}^{n}v_j^2}{n}} \tag{1}
```

```math
DR=20\log_{10}\left(\frac{V_{REF}}
{\sqrt{2}\,Gain\,IRN_{RMS}}\right) \tag{2}
```

```math
NFB=\log_2\left(\frac{V_{REF}}
{\sqrt{2}\,Gain\,IRN_{pp}}\right) \tag{3}
```

```math
ENOB=\log_2\left(\frac{V_{REF}}
{\sqrt{2}\,Gain\,V_{RMS}}\right) \tag{4}
```

CMRR評価では電池をLeCroy WaveStation 2012の正弦波へ置き換えた。単電源ADS1299へ合わせ、2.5 V DC offsetを持つ50 Hz、100 mV peakの正弦波を入力した。Tektronix TDS 2024Bで入力振幅を校正し、2分以上のデータとDFTからIRNを求め、式(5)でCMRRを計算した。

```math
CMRR=20\log_{10}\left(\frac{V_{OUT,P}}{V_{IN,P}}\right) \tag{5}
```

### EEG取得と処理

健常者12名がe-GlassとBiopac BN-EEG2を同時装着した。実験は約1時間で、各参加者は10分間の取得sessionを2回行い、その間に5分休憩した。各sessionは、(1) 開閉眼を含む自発EEG取得、(2) 着席・起立によって体動アーチファクトを起こす課題、の二つを含んだ。実験はDeclaration of Helsinkiに従い、Vaud州人対象研究倫理委員会の承認を受けた（project ID 2022-01338）。12名という標本数は、e-GlassのEEG取得信頼性を調べるpilot studyに適切と判断した [48]。

**Fig. 7. EEG取得。** (a) e-GlassとBiopacの同時取得実験。(b) e-GlassとBiopac電極を参加者の頭皮へ同時配置した例。

参加者へ手順を説明し、文書同意を得た。BN-EEG2はEEG pasteを用いるAg/AgCl cup電極、e-Glassは脂質除去のためalcohol清拭したsoft-dry電極を用いた。両装置の電極を隣接配置した。BN-EEG2は2チャネルだけのため、比較対象はe-GlassのF7とT7とした。同期triggerを両装置へ入力し、後処理で時刻を合わせた。e-Glassではanalog入力の一つでtriggerを取得し、optocouplerで絶縁して伝導雑音の混入を防いだ。

信号を4次Butterworth filterで1--30 Hzへ制限し、triggerに基づき課題別に分割した。自発EEGを目視でアーチファクト確認した。時間領域評価では、標本化周波数差をDTWで補正し、Session 1、Task 1の開眼・閉眼各60秒窓でPearson相関を求めた。周波数領域評価では、同sessionの閉眼3分間を4秒epochへ分け、Welch periodogramでPSDを推定した。装置間のspectral差はBland--Altman法で評価した [42]。

### e-Glassの応用

長期EEG監視は、個別化てんかん治療に必要な臨床情報 [43] と、CW推定のmarker [49] を提供できる。発作検出では感度、precision、F1、FAR/日を報告する。均衡データのCWMでは、これに特異度、正解率、感度と特異度のGmeanを加える。

```math
Sensitivity=\frac{TP}{TP+FN},\quad
Specificity=\frac{TN}{TN+FP}
```

```math
Precision=\frac{TP}{TP+FP},\quad
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
```

```math
F1=\frac{2\,Precision\,Sensitivity}{Precision+Sensitivity}
```

```math
FAR=\frac{FP\times24}{total\_time},\quad
Gmean=\sqrt{Sensitivity\times Specificity} \tag{6--7}
```

原文の式(7)の組版では`Gmean = sqrt(Sens · Prec)`のように見えるが、本文とTable 5は感度と特異度の幾何平均として説明しているため、ここではその定義を記した。両応用の学習・試験はMATLABとPythonを用いてオフラインで行った。

実装評価では、RTOS traceでthread実行時間を測り、FreeRTOS toolと動的確保量の手計算でRAMを見積もり、Otii Arc Pro [50] で機械学習実行中の平均電流を測定した。

#### てんかん発作検出

CHB-MIT Scalp EEG [15] を使用した。24名の小児患者から双極配置、256 Hzで取得され、982.9時間、注釈付き発作198件を含む。全被験者で共通する18チャネルと、e-Glassに相当するF7T7、F8T8だけの二条件を評価した。

EEGをzero-phase 4次Butterworth filterで1--20 Hzへ制限し、4秒窓、0.5秒step、87.5% overlapへ分割した。各窓・各チャネルから文献 [7] の56特徴を抽出した。TSCV [7] により時系列上の学習・試験を行い、最初のモデルには発作1件以上を含む最低5時間のEEGを要求した。Bayesian後処理 [7] の後、SZcore [51] でevent単位の性能を評価した。

#### 認知負荷モニタリング

CWMは、操作者の認知状態に応じて課題支援を調整し、HMIを改善できる。模擬捜索救助mission中に24名、平均`27.7 ± 4.8`歳から取得した内部データセット [46] を使用した。全EEG電極と、e-GlassのF7、T7、F8、T8の二条件を評価した。実験の詳細は先行する2021年論文 [23] に示される。

band-pass filterに加え、e-Glass用アーチファクト除去を使用した。最良条件は、56秒窓、60% overlap、200本の木からなるRF、30-fold RFECV後の18特徴であった。

## 結論

ウェアラブルによるリアルタイム脳活動監視は、日常環境でEEGを継続的、非侵襲的、個別的かつ長期に追跡し、てんかん発作検出からCWMまで幅広い健康用途を支えうる。

本研究は、神経疾患の個別監視を目的とし、目立たないEEG取得とリアルタイム処理を行うe-Glassを提示した。e-GlassはIFCNガイドライン [24] の条件を満たし、IRN 1.07 µV peak-to-peak、NFB 18.41 bit、高い入力インピーダンスとCMRRを示した。健常者pilot studyでは、研究用EEG装置と最大平均Pearson相関0.93を示した。

発作検出では、F7T7とF8T8の2双極チャネルだけで24名中11名に感度100%、平均感度63.8%、FAR 2.35件/日を得た。225 mAh電池で最大28.5時間、発作検出機械学習を実行できる。

CWMでは内部データセットの未知データに対して正解率74.5%、Gmean 74.0%を得た。これにより、勤務中の操作者認知状態を考慮するHMIへ応用できる可能性を示した。e-Glassは発作検出とCWMを含むリアルタイムEEG応用のためのウェアラブル基盤を提供する。

## データ利用可能性

発作データは公開CHB-MIT scalp EEG databaseから取得できる。

https://physionet.org/content/chbmit/1.0.0/

CWMデータセットはSwiss CER-VD project PB2017-00295でFabio Dell'Agnola、Ping-Keng Jao、Ricardo Chavarriaga、José del R. Millánが生成した。Millán教授の許可を得て合理的な要請により提供されうる。e-Glass取得データも責任著者への合理的な要請により提供されうる。

- Received: 2025年6月27日
- Accepted: 2025年11月20日

## 参考文献

参考文献1--51は書誌誤変換を避けるため、`eeg-glasses_original.md`の原文を参照する。

特に本論文との関係が深い文献は次の通りである。

- [4] Sopic et al. e-Glass: A Wearable System for Real-Time Detection of Epileptic Seizures (2018).
- [7] Zanetti et al. Approximate zero-crossing: a new interpretable, highly discriminative and low-complexity feature for EEG and iEEG seizure detection (2022).
- [17] Zanetti et al. Robust Epileptic Seizure Detection on Wearable Systems with Reduced False-Alarm Rate (2020).
- [22] Frey et al. GAPses: Versatile Smart Glasses for Comfortable and Fully-Dry Acquisition and Parallel Ultra-Low-Power Processing of EEG and EOG (2025).
- [23] Zanetti et al. Real-Time EEG-Based Cognitive Workload Monitoring on Wearable Devices (2022).
- [24] Nuwer et al. IFCN standards for digital recording of clinical EEG (1998).

## 謝辞

本研究は、European Union Horizon 2020 Marie Skłodowska-Curie（grant 754354）、e-Glass project（EPFL Enable project 6.1828）、Swiss NSF Edge-Companions（grant 10.002.812）、Swedish Research Council、Wallenberg AI, Autonomous Systems and Software Programの支援を一部受けた。また、Hong Kong SAR Government Innovation and Technology CommissionのInnoHK initiativeが支援するACCESS - AI Chip Center for Emerging Smart Systemsにおいて一部実施された。

著者らは、ウェアラブル発作検出に関する議論とe-Glass projectへの支援についてPhilippe Ryvlin教授へ、倫理承認取得と最新3D frame設計への支援についてJérôme Thevenot博士へ謝意を表する。

## 著者の貢献

R.Z.は実験を着想・実施し、データ解析と原稿初稿を担当した。A.A.はproject構想、方法提案、初稿の執筆・レビューを担当した。D.A.はprojectを構想し、監督、資源、最終原稿レビューを担当した。全著者が原稿を確認した。

## 宣言

### 競合する利益

著者らはリアルタイムてんかん発作検出用ウェアラブルシステムの特許を保有する（EPO EP3755219、2025年5月30日登録）。発明者はAmir Aminifar、Dionisije Sopic、David Atienza Alonso、Renato Zanettiである。

### 追加情報

資料請求はR.Z.へ連絡する。Springer Natureは地図上の管轄権主張と所属機関について中立を維持する。

本論文はCreative Commons Attribution 4.0 International Licenseで公開されている。適切な著者・出典表示、ライセンスへのリンク、変更の明示を条件に、利用、共有、改変、配布、複製が許可される。

