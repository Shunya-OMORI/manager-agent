# dog-mmwave-rri — ミリ波によるイヌの RR Interval 推定

2026年度（学部4年）の卒業研究の作業場所である。
2026-07-21、最終テーマを **「ミリ波を用いたイヌの RR Interval 推定」** に確定した。

## ファイル

| ファイル | 内容 |
|---|---|
| [先行研究調査_ミリ波の変位推定.md](先行研究調査_ミリ波の変位推定.md) | ミリ波が測る物理量である**変位**の側から先行研究を切り直した調査（2026-07-17 作成）。ヒト／イヌ／他生物 11 種以上を網羅し、空白の位置を判定している。テーマ確定前の文書であり、**RR Interval を目的変数に置いた現テーマの視点では未整理の部分がある** |
| [調査_入力設計とアーチファクト除去.md](調査_入力設計とアーチファクト除去.md) | **（2026-07-21 追加）** 信号処理をモデル入力設計へ持ち込む方向の調査。研究室の系譜（田中・Han・入交）と連携研究者（Mandic・Lotte・Arvaneh）の手法を、ミリ波の困難（呼吸高調波・RSA・体動）へ接続する。**卒論の芯の三案と推奨を含む** |

## 入手できるデータセット（2026-07-21、S. Han 先輩より）

先輩の Han さんから、参考にしている論文とデータセットの組を教えていただいた。
**いずれも未取得である。ユーザの指示によりダウンロードは保留している。**

| モダリティ | 論文 | データ | 対象 | 拍単位の正解 |
|---|---|---|---|---|
| **ミリ波** | Chen et al., "Contactless Electrocardiogram Monitoring With Millimeter Wave Radar," *IEEE Trans. Mobile Computing*, 2022, DOI: [10.1109/TMC.2022.3214721](https://ieeexplore.ieee.org/abstract/document/9919401)（プレプリント [arXiv:2112.06639](https://arxiv.org/abs/2112.06639)） | [MMECG（GitHub: jinbochen0823/RCG2ECG）](https://github.com/jinbochen0823/RCG2ECG) | **ヒト** 35名 | **あり**。心電事象のタイミング誤差 中央値 **14 ms 未満** |
| **UWB** | Ahmed et al., *Scientific Data* 11:107, 2024 → [03_Ahmed-2024](summaries/03_Ahmed-2024_dog-uwb-public-dataset.md) | [Figshare 23820915](https://figshare.com/articles/dataset/Dogs_Vital_Sign_Dataset/23820915/1) | **イヌ** 30頭 | **なし**（1 FPS 平均） |
| **CW** | Schellenberger et al., "A dataset of clinically recorded radar vital signs with synchronised reference sensor signals," *Scientific Data* 7:291, 2020, DOI: [10.1038/s41597-020-00629-5](https://www.nature.com/articles/s41597-020-00629-5) | [Figshare 12186516](https://figshare.com/articles/dataset/A_dataset_of_clinically_recorded_radar_vital_signs_with_synchronised_reference_sensor_signals/12186516) | **ヒト** 30名 | **あり**（心電図・インピーダンス心図・連続血圧を同期） |

### 各データセットの要点（未精読、書誌と公開情報の範囲）

**MMECG（ミリ波・ヒト）** — TI AWR1843 ＋ DCA1000。開始周波数 77 GHz、総帯域 3.32 GHz、
**フレームレート 200 Hz**、12 チャネル仮想アレイ（3Tx×4Rx）。35名（男22・女14、18--65歳）、
公開分 4.55 時間。仰臥位、4 つの生理状態（通常呼吸・不規則呼吸・運動後・睡眠）、1 試行 3 分。
`.mat` 形式で **RCG（4 次元の心臓運動）**、同期 ECG、3 次元位置座標、被験者属性を含む。
**心電事象のタイミング誤差が中央値 14 ms 未満**、形態の Pearson 相関 中央値 90%、RMSE 0.081 mV。

**Schellenberger（CW・ヒト）** — Six-Port 方式の連続波レーダ、ISM 帯 **24 GHz**。
健常者30名、**同期データ 24 時間**。参照装置が心電図・インピーダンス心図・非侵襲連続血圧を同時計測。
被験者は傾斜台に横たわり、**血行動態と自律神経系を賦活する 5 つのシナリオ**を実施。

## 先行研究の要約

要約は `summaries/` に 1 論文 1 ファイルで置く．形式は `rules/reading-paper.txt` の列順に従い，
末尾のテーマ固有列を（o）使用機材と実験条件／（p）正解データと評価指標／（q）本テーマへの含意とする．
PDF 原本は `papers/` に置くが，`.gitignore` により追跡しない．

### 作成済み

| ファイル | 論文 | 一言 |
|---|---|---|
| [01_Bowden-2024](summaries/01_Bowden-2024_canine-mmwave-hr-depth-camera.md) | Remote Heart Rate Estimation of Canines using a mmWave Radar and Depth Camera（IEEE Sensors Letters 2024） | **最も近い先行研究**．77 GHz を覚醒下のイヌ4頭へ．従来 DSP は Pearson 0.010 と無相関，ハイブリッド DSP-LSTM で RMSE 13.9 bpm・0.76 |
| [02_Wang-2020](summaries/02_Wang-2020_dog-cat-uwb-vital-signs.md) | Non-Contact Vital Signs Monitoring of Dog and Cat Using a UWB Radar（Animals 2020） | **新規性の最大の脅威に見えるが限定的**．「拍対拍間隔が類似」は麻酔下1頭の図の目視所見で定量検証なし．UWB 7.29 GHz |
| [03_Ahmed-2024](summaries/03_Ahmed-2024_dog-uwb-public-dataset.md) | A public dataset of dogs vital signs recorded with UWB radar and reference sensors（Scientific Data 2024） | **公開データセット**．イヌ30頭・臨床承認済み獣医用心電図センサ．ただし 1 FPS 平均で拍単位情報なし |

### 3 件から見えた最重要の事実

**イヌを対象に，拍単位の RR Interval をレーダで定量的に推定し検証した研究は存在しない．**
3 件はいずれも平均心拍数（bpm または Hz）で止まっている．
拍間隔に触れた唯一の記述である Wang ら（2020）の Figure 5d 図注も，
麻酔下 1 頭の図の目視所見であり，著者自身が「さらなる特性評価を要する」と留保している．

同時に，難易度の高さも裏づけられた．Bowden ら（2024）は覚醒下のイヌで
従来型 DSP のピーク計数が **Pearson 0.010** という無相関を記録している．
平均心拍数は誤差が平均化されるが，**RR Interval は平均化できない**．

### 未作成の候補

**A. イヌ×レーダ**
- Amano Rina「FMCW Radar-Based Monitoring of Canine Vital Signs Validated Using IMU」法政大学大学院紀要 情報科学研究科編 19, pp.1-9, 2024, DOI: 10.15002/00030601（**FMCW＋IMU 検証．50 cm で心拍 6.90 bpm 誤差**）
- RayPet（FMCW ミリ波点群でイヌの姿勢分類 89%，2024）
- ペット顔動画からの非接触心拍計測（Front. Vet. Sci. 2024）

**B. 動物×レーダ** — マカク（Sci. Rep. 2024），Sakamoto レビュー（IEICE 2024），獣医リモート計測レビュー（PMC11988085），ウォンバット 79 GHz，ウマ，げっ歯類 60 GHz，ラット RRV，チンパンジー，家畜センシングレビュー

**C. ヒト×ミリ波の拍間隔・HRV（手法の移植元）** — FMCW HRV（Sensors 2025, IBI 誤差を 50% 超削減），cardiac beamforming による非接触 SCG・HRV（Front. Physiol. 2025），radarODE，AirECG，LifWavNet，MultiVital，PrivyWave

**D. 信号処理の課題** — レーダバイタルレビュー（PMC7085680），RBM 補償レビュー（Gouveia ら, Sensors 2019），Pi-ViMo，FMCW 変位確度（Appl. Sci. 15(6) 3316）

**E. イヌの RR Interval の生理・臨床** — 犬猫心電図学 HRV 章（Wiley），**イヌの RSA は平均心拍の 40.1%±4.5%（出典の一次確認が必要）**，Boxer の RR 間隔 Poincaré（PMC3184837），行動と HRV（Appl. Anim. Behav. Sci. 2025），HRV による情動予測（2016），イヌの福祉生理指標レビュー（2025）

## テーマ確定までの経緯

検討過程は [`research/archive/dog-human-comm/`](../archive/dog-human-comm/) にある。
却下した案とその理由は [`research/archive/README.md`](../archive/README.md) にまとめた。

先行調査から現テーマへ引き継ぐ主な論点は次のとおりである。

- **動物側の変位推定は例外なく「静止個体」に限定されている。**
  イヌ・ネコは睡眠中、ラットは麻酔下、ウマは起立静止である。
- **動物で得ている量は「呼吸数・心拍数」という周期のスカラ値に潰れている。**
  RR Interval のような拍ごとの量を対象にした報告は見当たらない。
- **運動中は心拍がどのモダリティでも取れない**（加速度計の利得も LRC により崩壊する）。
  ゆえに対象とする行動条件の限定が要る。
- **アンラップに要る標本化率 f_s > 4v/λ** という制約 C は、
  静止個体への限定を説明する物理的根拠である。

## 未確定の事項

- **モダリティが未確定である（2026-07-21 判明）。**
  Han 先輩によれば、ミリ波にするかはまだ確定ではない。候補はミリ波・UWB・CW の三つである。
  本ディレクトリ名 `dog-mmwave-rri` はミリ波を前提としているため、
  **確定後に改名が必要になる可能性がある**。
- RR Interval の正解をどの接触センサで取るか。
  候補は Polar H10（Bowden らが使用）と BM7Vet Pro（Ahmed らが使用、臨床承認済み）。
- 対象とする行動条件（安静・睡眠・起立静止のいずれか、またはその範囲）。
- 使用するミリ波レーダの周波数帯と、研究室の保有機材の確認。
- **卒論の芯をどの方針に置くか**（[調査_入力設計とアーチファクト除去.md](調査_入力設計とアーチファクト除去.md) の三案）。
- **入交眞巳先生（獣医行動学、動物医療センター）との連携の実態。**
  Han らの論文の共著者であり、イヌのデータ取得の可否を左右する最大の要因。
- **イヌの RSA が平均心拍の 40.1%±4.5% とされる値の一次文献。**
  周波数領域の枠組みが不利であるという中心的な論拠が、この値に依存する。

## 現在の状態

作業場所を作成した段階である。実験計画は未着手である。
