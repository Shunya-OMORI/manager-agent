# 雑誌会template

- Source PDF: `C:\Users\Projects\manager-agent\rules\雑誌会template.pdf`
- Extraction: `PyMuPDF` page-by-page text fallback
- Verification status: unverified draft

- Page count: 31
- Title metadata: 雑誌会20260529_imamura25
- Author metadata: 

---

## Page 1

IEEE Journal of Biomedical and Health Informatics (2026)

M4CEA: A Knowledge-guided Foundation Model for
Childhood Epilepsy Analysis





Yuanmeng Feng1, Dinghan Hu1, Tiejia Jiang2, Feng Gao2, Jiuwen Cao1

1. Machine Learning and I-health International Cooperation Base of Zhejiang Province, and
   the Artificial Intelligence Institute, Hangzhou Dianzi University, Zhejiang, China
2. Department of Neurology, the Children’s Hospital, Zhejiang University School of Medicine,
   National Clinical Research Center for Child Health, Hangzhou, China

                      今村聡志                               2026/05/29 M1
                                                                                                                                      1

## Page 2

概要


 ■ 背景：小児てんかん解析には多様な EEG タスクが存在するが，既存の EEG 基盤モデルは小児

    の年齢依存的な特性を考慮していないため，適用が困難  EEG

 ■ 目的：小児てんかん解析における複数タスクを単一モデルで処理できる EEG 基盤モデルの構築

 方法： ■

   ■ 4 施設から収集した約 1,000 時間の小児 EEG で事前学習

  エントロピーに基づくマスキングと学習可能な時間位置埋め込みを導入   ■

  振幅と位相を再構成目標とした自己教師あり学習   ■

 結果 ■

   ■ 全 8 つの下流タスクで比較手法（LaBraM 等）を凌駕

   ■ Grad-CAM による可視化で，モデルの注目領域が神経科医のアノテーション領域と一致





2

## Page 3

てんかん


  幼少期において特に有病率の高い神経疾患の一つ  ■

  合併症：知的障害，発達障害  ■

  ■ 脳波（Electroencephalogram; EEG） による診断が主流


     生後 年まで          歳 －  歳         歳 －  歳              1                       1     12                  11     17

       件  万人          件  万人         件  万人         102      / 10                   102      / 10               21–24      / 10
            =           >





3

## Page 4

てんかんにおける   解析手法            EEG


                タスク特化深層学習モデル       基盤モデル    手動特徴量モデル

 ドメイン知識から人手で     教師あり学習により       自己教師あり学習により
                                 特徴を獲得    特徴量を設計         特徴を獲得           EEG  EEG                  EEG



                 手動設計が不要                                ラベル依存を大幅に低減  ✗ 計算コストが高い        ✓                                         ✓

                                複数タスクへ適用可能                            ✗ 大量のラベル付き EEG     ✓

                が必要                                                      ✗ 既存の基盤モデルは小児

                            ✗ 単一タスクに特化         EEG を考慮していない





4

## Page 5

小児てんかん   の解析における課題         EEG


 小児特有の脳波特性：小児の脳波は成長とともに変化するため，成人の脳波とは異なり複雑

   非対称から対称へ                                   [Kaminska+, Handbook of clinical neurology, 2019]    ■

   不規則から規則的へ    ■


 多岐にわたる臨床タスク

   発作検出・分類，てんかん症候群分類，睡眠段階分類など    ■

   タスク間は相互に関連しているため，包括的に理解できるモデルが必要    ■


 大規模な小児   データセットの欠如          EEG


           小児てんかん解析に特化した基盤モデルの構築が必要




5

## Page 6

提案手法：M4CEA

 ■ 振幅変動を考慮した時間位置埋め込みの導入（Learnable-time-positional Embedding）

 ■ エントロピーに基づくマスク戦略の導入（Knowledge-guided Mask Strategy）

 ■ 1,092.3 時間の小児 EEG による事前学習





6

## Page 7

Learnable-time-positional Embedding

 ■ 知見：小児 EEG の振幅は年齢とともに変化するため，時間領域に豊富な情報を含む

 方法：振幅変動を考慮した学習可能な時間位置埋め込みの導入 ■

   学習可能な時間位置埋め込み を用意    1.                                            ϵt
   パッチ  の移動平均と の要素積  を計算    2.                   pi,j                  ϵt         ϵP

   パッチ  の畳み込み出力と  を加算    3.                   pi,j                 ϵP





7

## Page 8

Knowledge-guided Mask Strategy

 ■ 知見：エントロピーは EEG の複雑性を反映（特に小児 EEG）[Lawhern+, J. Neural Eng., 2018]

 ■ 手法：Multi-scale Fluctuation-based Dispersion Entropy (MFDE) [Azami+, IEEE Access, 2019] を 

 マスク確率に使用

   情報密度が高い複雑なパッチを優先的にマスク →





8

## Page 9

事前学習


 ■ 知見：小児 EEG は発達途上で不安定であるため，生信号の再構成による事前学習は困難
                                                                                        [França+, Nat. Commun., 2024]
 方法：マスクされたパッチにおける振幅と位相の再構成誤差を最小化 ■





9

## Page 10

下流タスク（8 種類）


  施設          タスク名           タスク内容   セグメント長

       オンセット検出（OD）                2 クラス分類
   HUH
       アーチファクト検出（AD）              6 クラス分類

   Cork  低酸素性虚血性脳症の重症度分類（HIEG）   4 クラス分類
                                                                   4s
   CHSZ  発作型分類（STC）                   4 クラス分類

       発作型分類（STC）                   4 クラス分類

       小児てんかん症候群分類（CES）          7 クラス分類

  CHZU  睡眠段階分類（SSC）                 3 クラス分類

       てんかん様活動の検出（EAD）       セグメンテーション     30s

       棘徐波指数の定量化（SWIQ）        セグメンテーション



10

## Page 11

ファインチューニング（下流タスクごと）

 分類タスク： ■





 ■ セグメンテーションタスク（EAD・SWIQ）：





11

## Page 12

下流タスクにおける結果（抜粋）


        タスク名         指標    M4CEA     SOTA    差分

 オンセット検出（HUH-OD）                    0.968       0.874      9.4%

 アーチファクト検出（HUH-AD）                 0.809       0.699     11.0%

  HIE 重症度分類（Cork-HIEG）                   0.940       0.769     17.1%

 発作型分類（CHSZ-STC）               Bal.Acc.    0.942       0.932      1.0%

 発作型分類（CHZU-STC）                     0.984       0.961      2.3%

 小児てんかん症候群分類（CHZU-CES）            0.956       0.604     35.2%

 睡眠段階分類（CHZU-SSC）                    0.964       0.920      4.4%

 てんかん様活動の検出（CHZU-EAD）     Sens.     0.735       0.540     19.5%

 SWK 定量化（CHZU-SWIQ）         PCT-10    0.958       0.804     15.3%



12

## Page 13

アブレーション：マスク確率

 ■ マスク確率：25%, 50%, 75%

 考察： ■

  大域的な特徴を捉える必要があるタスク（左二つ）には高いマスク確率が適する   ■

  局所的な特徴を捉える必要があるタスク（右二つ）には低いマスク確率が適する   ■

          大域的                    局所的

   発作型分類     睡眠段階分類     てんかん様活動検出  棘徐波指数の定量化





13

## Page 14

アブレーション：マスク戦略と時間位置埋め込み


                                                ■Learnable-time-positional Embedding (LTPE)
    手法     発作型分類  睡眠段階分類   ■学習可能にすることで性能向上
                        ■位相の再構成品質が向上   KGM＋LTPE
                   0.979       0.982
  （提案手法）                             ■Knowledge-guided mask strategy (KGM)
   KGM＋FTPE                 ■エントロピーに基づくマスク戦略のみではラ
                     0.974        0.965
 （固定埋め込み）                 ンダムマスクを下回る

    RM＋LTPE                         ■LTPE と組み合わせることで性能向上                     0.972        0.978
 （ランダムマスク）
                        ■損失の推移が安定

    KGM のみ        0.976        0.975



    RM のみ         0.977        0.978





14

## Page 15

による可視化Grad-CAM

 ■ Gradient Weighted Class Activation Mapping (Grad-CAM): モデルの予測に寄与した入力信号の
 領域を可視化する手法

 タスク：てんかん様活動検出 ■

 ■ 比較モデル：LaBraM，Patch TST

 ■ 結果：M4CEA が最も多く 
 専門医のアノテーションと一致





                          青枠：専門医によるアノテーション 赤枠：モデルの注目領域


15

## Page 16

考察


 ■ Knowledge-guided mask strategy の効果： 
 情報密度の高いパッチを優先的にマスクすることで，モデルが強制的に臨床的に意味のある特徴
 を学習

 ■ Learnable-time-positional Embedding の効果： 
 サンプルに対して固定の時間情報を付与しないことで，データセット間のサンプリング周波数の
 違いを吸収

 ■ 事前学習データの効果：LaBraM などと異なり小児 EEG を用いて事前学習することで，小児

    特有の年齢依存的な特徴を学習  EEG





16

## Page 17

研究の限界と今後の課題


 ■ 1,000 時間の事前学習 EEG は今日の大規模医療 FM と比較して小規模 

   より大規模な小児   コーパスが必要 →            EEG


 ■ 下流タスクごとにフルファインチューニングが必要であるため，計算コストが高い 

   パラメータ効率が良い手法の導入が必要 →


 ■ モデルが EEG にのみ対応 

     や臨床テキストなどの他のモダリティとの統合 → ECG





17

## Page 18

まとめ


 ■ 小児てんかん解析のための EEG 基盤モデルである M4CEA を提案

 エントロピーに基づくマスク戦略と学習可能な時間位置エンコーディングが有効 ■

 ■ チャンネル数・信号長が異なる EEG に対してファインチューニング可能

 ■ 全ての下流タスクにおいて SOTA を上回る性能

 ■ Grad-CAM による可視化で，モデルの注目領域が神経科医のアノテーション領域と一致





18

## Page 19

コメント


 公開されているコードの実装と論文とで一致しない部分が多くて困った ■

 エントロピーベースのマスクは自分もやってみたい ■

 ■ EEG のサンプリング周波数が一定じゃないのに下流タスクで上手くいってるのが不思議

 ■ LaBraM の後継モデルである NeuroLM の論文内で位相の再構成は学習にあまり貢献しないと書
 かれていたが，この論文内では効果的だったのが気になった





19

## Page 20

Appendix





20

## Page 21

振幅の分散（Hjorth activity）に基づく考察

                       ■方法：
                       ■切り出したパッチごとに振幅の分散を計算
                        ■隣接する年齢群同士の分布を比較
                       ■結果：

                         ■各年齢群間に有意差が見られた（t-検定）

                                        ■Normal グループ：年齢が上がるにつれて減
                        少する傾向





21

## Page 22

Multi-scale Fluctuation-based Dispersion Entropy



                              のパッチを一定の窓幅（）で区切り，各窓の平均値を計算                                                               a. EEG                                                                                  τ

                                               の範囲に写像                                                               b. 正規累積分布関数（NCDF）を用いて                                                                                               (0,1)                                    a.
                              の整数に量子化                                                                    c.                                             1 −c

                            窓幅 ，ストライド で差分パターン列 を作成                                                               d.                                  m          d              π

                            差分パターン列の出現確率 を求める                                                               e.                                                     P         b.       c.

                            エントロピーを計算                                                                                               f.



   d.

                                                   e.                                        f.





22

## Page 23

学習時の損失関数


 ■ 事前学習：フーリエ変換された振幅（Magnitude）と位相（Phase）の再構成誤差を最小化

                   N               1                           2       Lossmag =      (Resmag −Rawmag)      ∑           N                     n=1
                   N               1                             2       Lossphase =       (Resphase −Rawphase)      ∑           N                     n=1

 ファインチューニング：各タスクごとにクロスエントロピー損失を計算 ■


                  （ は真のラベル， はモデルの予測値）       Lossfine−tuning = −∑y log ̂y     y                          ̂y





23

## Page 24

データセット


                 NicoletOne V32 video 
                                                           NicOne EEG amplifier, EEG cap (Waveguard, ANT-Neuro)
            EEG instrument


                     名                                 134

                                            名                                                                            79




                     名                                     9
                                 計測機器不明



                                            名                                                                            27


                    名                                  64                                                                  NicoletOne / Neurofax



                        名                                                名                                        69                                                                                    53





24

## Page 25

前処理


  フィルタリング： 1.

   ■ 50 Hz ノッチフィルタ

   ■ 0.5–70 Hz バンドパスフィルタ

  リサンプリング： 2.

   ■ CHZU: 1000 Hz のまま

   ■ CHSZ: 500/1000 Hz   500 Hz          →
   ■ HUH: 256 Hz   200 Hz       →
   ■ Cork: 200/256 Hz   200 Hz         →
  振幅を  パーセンタイルで正規化 3.       95





25

## Page 26

アブレーション：事前学習の有無


 ■ 方法：事前学習＋ファインチューニングの場合とタスク特化で 1 から学習の場合を比較

 結果：事前学習＋ファインチューニングの場合が一貫して高い性能を示した ■





26

## Page 27

アブレーション：ファインチューニングの有無


 方法：ファインチューニングの場合と線形プロービングの場合で比較 ■

 ■ 結果：睡眠段階分類では性能差が小さかったものの，総合的にファインチューニングの場合が 
 優位





27

## Page 28

時間位置埋め込みの可視化


 ■ Fixed-time-positional embedding は周期的なパターン 

   サンプル番号に対して固定であるため，異なるサンプリング周波数に対応できない →

 ■ Learnable-time-positional embedding は非周期的なパターン 

   柔軟な   の表現学習が可能 →     EEG





28

## Page 29

事前学習用パラメータ


 ■ オプティマイザ：AdamW

 ■ オプティマイザのパラメータ：             ，Weight Decay                         β = (0.9,0.999)         = 1 × 10−4

 ■ 初期学習率：            1 × 10−3
 ■ 学習率スケジューラ：ウォームアップエポックを 30 としたハーフサイクルコサイン（half-cycle

  cosine）

 ■ バッチサイズ：256

 ■ エポック数：100





29

## Page 30

マスク方法別の再構成結果とロス推移の比較


提案手法の方が周波数領域においても時間領域においても再構成結果が良い





30

## Page 31

アブレーション：マスク確率





     発作型分類



    睡眠段階分類



 てんかん様活動検出



       定量化        SWI





31
