20260812 進捗報告

（1〜6 が本編です．付録は補足なので読み上げません）


前回（20260805）を振り返って
    • いただいたご指摘
        ○ イヌの「情動」を推定することは考えない方がよい．内部状態なら推定できる
        ○ RR 間隔から Arousal ではなく，交感神経・副交感神経
        ○ 情動までは特定できないが，内部状態の変化を見るためのセンシングは重要
    • 反省点：先生とシステムの要件を決めたかったのに，先に結果の話をしてしまいました
    • 今回は，引き継いだデバイスの説明と，先行研究の整理を先に置きます


1. 野田先輩からマルチモーダル計測デバイスを引き継ぎました

1-1. 装置の目的
    • イヌの心拍変動を日常生活で測ること
    • 心電図は剃毛とジェルが要るので，日常では使えない
    • そこで，装着負荷の小さいセンサと，正解になる心電図を同じイヌ・同じ時刻で測る
    • 正解つきのイヌの生体データを作るための装置です

1-2. 構成
    • 心電図アンプ AD8232 ×2 → 2 誘導
    • IMU（MPU6050）×4 → 6 軸 ×4 = 24 ch
    • ESP32S3 が I2C とアナログ入力をまとめる．
      通信は BLE ではなく ESP 専用の高速通信で，BLE のボトルネックを回避している
      （受信側の実装までは聞いていません）
    • 映像と音声はキャプチャボードで別に取り，LSL で時刻を合わせる

1-3. 装着方法
    • 心電図：先に包帯を巻き，その中にジェルを入れて電極を挟む
      配置は 右肩＝グラウンド，左肩＝リファレンス，胸の中央，腹の中央
    • IMU：ハーネスにマジックテープで留める
    • ハーネスは伸縮素材で密着させ，包帯と同じ巻き方ができ，センサを足しやすい構造

1-4. 教わったこと・受け取ったもの
    • ハーネスの装着方法，包帯の巻き方，電極配置
    • IMU・電池ボックス・基板本体の固定の仕方，回路の簡単な説明
    • 実装に必要な工具，部品


2. 回路の修理

    • 電源入力コネクタのワイヤが断線しかけていた
        ○ スンウさんから電源が不安定という報告があり，そこを疑って確認した
        ○ ワイヤを切断し，新しいコネクタを付け直した
        ○ 電池ボックスの重さと，運搬時にケーブルへ強い力がかかることが原因と考え，
          コネクタ付近（被覆まわりなど）をグルーガンで補強した
    • 心電図用のボタン電極（ディスポ電極をはめる側）が錆び切っていた
        ○ 新しいボタンをはんだ付けした
        ○ 再度錆びないよう，ボタン上面（接触面でない側）をグルーガンでコーティングした


3. KAMEC

    • KAMEC 内 PC について説明を受けました
    • 記録の開始方法，研究室 NAS へのデータの送信方法を学びました


4. 先行研究の整理

    このデバイスをどう発展させるかを考える前に，イヌの心拍計測がどこまでできていて，
    どこからできていないのかを調べました．根拠と URL は付録 A にまとめてあります．

    できていること
        • 心拍数（分単位の平均）は，条件を絞ればおおむね取れている
        • ドライ電極（毛をかき分けるピン電極）は，立位・座位なら拍の 68〜95% を検出
          ［Virtanen ら, Sensors, 2018．ヘルシンキ大］
        • 首輪の加速度センサからの心電図再構成は，安静・睡眠に限れば F1 0.867
          ［Foster ら, ACI 2021．ノースカロライナ州立大 Bozkurt 研］
        • 呼吸数は，繊維センサ・映像・IMU など複数の方法で取れている
        • 非接触も，麻酔下のイヌなら参照心電図つきの公開データセットがある
          ［Ahmed ら, Scientific Data, 2024．漢陽大］

    できていないこと
        • 動いているイヌで落ちる
            ○ 同じドライ電極の検出率が，歩行では 45〜57% まで下がる
            ○ 市販スマート首輪と 24 時間ホルターの比較（健康なイヌ 12 頭）では，
              24 時間平均の心拍数は使えるが，2 分間の心拍数は一致が悪く，
              記録可能時間の 43% ではそもそも心拍を出力できていない
              ［Gunasekaran & Sanders, J Vet Cardiol, 2025．ミシガン州立大］
        • 拍ごと（RR 間隔）の精度を検証した研究がほとんどない
            ○ ドライ電極の研究も検出率までで，HRV は算出していない
            ○ 本学の獣医の先生方のレビューでも，拍ごとの検証データと種ごとの校正法が
              足りないと整理されている［Zhao, Tanaka R. ら, Animals, 2025］
            → 交感神経・副交感神経を見るには RMSSD が要るのに，そこが未検証です
        • なお，HRV から情動を読む研究はありますが（Katayama ら, 2016．麻布大・奈良先端大），
          最近のレビューは指標の妥当性そのものを問題にしています．
          先生のご指摘どおり，交感・副交感の活動までにとどめるのが妥当だと考えています

    まとめ
        • 隘路は「覚醒して動いているイヌで，拍ごとの正解となる心電図を安定して取ること」
        • 野田先輩のデバイスは，そこに一番近い位置にあります


5. デバイスの拡張案

    ミリ波を使う案は 4 つのうちの 1 つです．どの案でも，正解の心電図の質が上限を決めます．

    案 1: 接触の良し悪しを記録しながら測る
        • いまは電極が毛で浮いたかどうかが記録に残らず，歩行で検出率が半分になる理由も
          事後には特定できない
        • 電極-皮膚インピーダンスを心電図と同時に記録する．
          ヒトのウェアラブルでは，これを参照信号にした適応フィルタで体動アーチファクトを
          除去する手法が確立している．まず AD8232 のリード外れ検出から確認する
        • 正解の心電図に品質のラベルが付き，学習に使える区間を選別できる
          → スンウさんの IMU から心拍を推定する研究に，そのまま効きます
        • 難しさ：アナログ回路の追加．ESP32S3 でどこまで完結できるかは未確認

    案 2: 加速度センサをイヌのどこに置くか決める
        • ヒトでは胸壁に 36 個の加速度計を並べて心臓振動の空間分布を測り，最適位置を
          決めた研究がある［J Cardiac Failure, 2020］．イヌでは首輪 1 点だけ
        • 野田先輩のデバイスは IMU が 4 個あるので，位置を変えて同時記録し，
          イヌの胸壁で心拍の振動がどこで一番よく出るかを測る
        • モデルを変えずに入力の質が上がる．難しさは装着の再現性と体格差

    案 3: 毛の障壁を，電気以外の経路で越える
        • 圧電センサによる BCG は，覚醒したイヌでも心拍数の相関 0.97
          ［Chuluunbaatar ら, Veterinary Sciences, 2025．12 頭］
        • 電位ではなく機械振動で拾う経路を足す
        • ただし BCG も報告は心拍数までで，RR 間隔の精度は出ていない

    案 4: 非接触センサを足す（ミリ波はここに入ります）
        • レーダで取れているのは麻酔下か，呼吸だけ
        • 覚醒下で正解の心電図が取れる野田先輩のデバイスと同時に記録する
        • 難しさ：KAMEC に置けるか，心電図と時刻を合わせられるか


6. ご相談したいこと

    • 内部状態として，何をどこまで推定すべきか
        ○ 心拍数までで足りるのか，RMSSD（副交感神経の指標）まで要るのか
        ○ 要るなら，拍ごとにどれくらいの精度が必要か
    • デバイスに何を足すべきか（案 1〜4 のどれから着手するか）
    • KAMEC の計測環境について
        ○ 非接触センサを置く場合の設置場所・電源・同期
        ○ 剃毛した心電図をどの程度の頻度・頭数で取るか
    • 家庭設置型の IoT デバイスに向けて，いまハードウェア・エッジ側に
      解決してほしい課題は何か


次回までにやること
    • 修理したデバイスの動作確認（電源，心電図波形，IMU 4 個すべて）
    • KAMEC で短時間の記録を通しで一度やってみる
    • 相談の結果に応じて，案 1 か案 2 の予備実験の手順を書き出す


────────────────────────────────────────
以下，付録
────────────────────────────────────────


付録 A. 調べた先行研究

A-1. イヌに装着して心電図を取る（電極の側）
    • Virtanen ら, "Evaluation of Dry Electrodes in Canine Heart Rate Monitoring,"
      Sensors 18(6):1757, 2018．ヘルシンキ大
      スプリングピン 37 本／Ag-AgCl ポリマー 30 ピン／金メッキピン 12 本の 3 種を 3 頭で比較．
      検出率は 立位 68〜93%，座位 76〜95%，伏臥 61〜75%，歩行 45〜57%．
      毛の厚さ・姿勢による胸郭の形の変化・ピン密度・接触圧が原因と考察．HRV は未算出
      https://doi.org/10.3390/s18061757
    • "Investigating Textile-Based Electrodes for ECG Monitoring in Veterinary Clinical Practice,"
      AUTEX Research Journal, 2022．銀めっき編み地 20×40 mm，弾性胸ベルト．
      軽い皮膚前処理ありで Ag/AgCl と同等の波形
      https://doi.org/10.2478/aut-2022-0027
    • Brugarolas, Latif, Dieffenderfer, Walker, Yuschak, Sherman, Roberts, Bozkurt,
      "Wearable Heart Rate Sensor Systems for Wireless Canine Health Monitoring,"
      IEEE Sensors Journal 16(10):3454-3464, 2016．ノースカロライナ州立大．
      心電図＋光電脈波＋IMU．導電性ポリマーで電極を被覆，光ファイバで皮膚への光結合を改善
      https://doi.org/10.1109/JSEN.2015.2485210

A-2. 装着型センサから心拍を推定する（モデルの側）
    • Foster, Wang, Williams, Roberts, Bozkurt, "ECG and Respiration Signal Reconstruction
      from an IMU at Various Orientations during Rest or Sleep for Dog Welfare Monitoring,"
      ACI 2021（第 8 回 Animal-Computer Interaction 国際会議）．ノースカロライナ州立大．
      首輪 IMU，12 通りの向き，安静・睡眠のみ．心電図再構成 F1 0.867／心拍数精度 0.913，
      呼吸 F1 0.726／呼吸数精度 0.893．自作の無線心拍センサで IMU と参照心電図を同期取得
      https://doi.org/10.1145/3493842.3493905
    • "Motion-Resilient ECG Signal Reconstruction from a Wearable IMU through Attention
      Mechanism and Contrastive Learning," ACI 2022．上記の体動下への拡張
      https://doi.org/10.1145/3565995.3566037
    • Lu, Cai, Stefanov, Chen, "Vib2ECG: A Paired Chest-Lead SCG-ECG Dataset and Benchmark
      for ECG Reconstruction," arXiv:2603.15539, 2026．
      ヒト 17 名・胸部 6 か所の IMU・12 誘導心電図．0.364 M の U-Net．
      電気的活動のない場所に波形を作る「幻覚」が未解決の課題として挙げられている
      https://arxiv.org/abs/2603.15539
    • Han S. ら, "A lightweight multi-feature fusion deep learning architecture for human ECG
      reconstruction from chest-worn accelerometer," ITC-CSCC 2025, Best Paper．本研究室
    • "Documenting Spatial Variation of SCG Signals for Optimal Sensor Placement,"
      J Cardiac Failure, 2020．ヒト 15 名の胸壁に加速度計 36 個．最適位置は左胸骨下縁
      https://www.sciencedirect.com/science/article/abs/pii/S1071916420312161

A-3. 市販デバイスの限界
    • Gunasekaran & Sanders, "Assessment of heart rate measurements obtained from a smart
      collar compared to 24-h Holter monitoring in healthy dogs," J Veterinary Cardiology, 2025．
      ミシガン州立大．健康なイヌ 12 頭．24 時間平均心拍数はバイアス 2.2 bpm（一致限界 -5.1〜+9.6）
      で臨床的に有用．一方 2 分間の心拍数は安静時・活動時とも一致が悪く，
      記録可能時間の 43%（範囲 24〜79%）で心拍を出力できず
      https://pubmed.ncbi.nlm.nih.gov/39675258/

A-4. 非接触計測
    • Ahmed, Yoon, Cho, "A public dataset of dogs vital signs recorded with ultra wideband
      radar and reference sensors," Scientific Data 11:107, 2024．漢陽大．
      シナリオ1＝麻酔下で臨床参照センサ（心電図含む）と同期，相関 0.9 以上．
      シナリオ2＝覚醒・自由行動だが参照は映像のみ
      https://doi.org/10.1038/s41597-024-02947-4
    • Zhang, Hu, Chen ら, "Contactless vital signs monitoring in macaques using a mm-wave
      FMCW radar," Scientific Reports 14:13863, 2024．ケージにレーダを設置．
      覚醒・麻酔の両方で，心拍数の平均絶対誤差 0.77 bpm，呼吸数 1.29 回/分
      https://doi.org/10.1038/s41598-024-63994-w
    • Zhao, Tanaka R., Mandour, Shimada, Hamabe, "Remote Vital Sensing in Clinical Veterinary
      Medicine: A Comprehensive Review," Animals 15(7):1033, 2025．本学（農工大）獣医．
      毛は rPPG の強い障害，レーダは体動に弱い，心拍と呼吸・体動の分離が依然困難，
      拍ごとの臨床検証データと種ごとの校正法が不足，と整理されている
      https://doi.org/10.3390/ani15071033
    • Rahman ら, "From video to vital signs: a new method for contactless multichannel
      seismocardiography," npj Cardiovascular Health, 2025．
      胸に貼ったマーカを 60 fps のカメラで追跡．心拍数の誤差 0.04 ± 2.14 bpm．
      ただし裸の皮膚が必要なので，イヌにはそのままでは使えない
      https://doi.org/10.1038/s44325-024-00034-6

A-5. 呼吸（比較のため）
    • "Smart Garment for Continuous Respiration Monitoring in Canines," ACS Sensors, 2025．
      導電性繊維の伸縮センサを胸に巻き，パンティング中の呼吸を計測
      https://doi.org/10.1021/acssensors.5c03783
    • "Audio and video nearables for monitoring respiratory rate in sleeping dogs,"
      Scientific Reports, 2025．側方からの映像が最良で RMSE 1.1 回/分，MAE 0.7 回/分
      https://doi.org/10.1038/s41598-025-25305-9
    • Chuluunbaatar ら, "Clinical Application of Monitoring Vital Signs in Dogs Through
      Ballistocardiography," Veterinary Sciences 12(4):301, 2025．
      圧電センサ＋6 軸．覚醒ビーグル 6 頭・麻酔 6 頭．覚醒時 心拍数 r=0.97，呼吸数 r=0.78
      https://doi.org/10.3390/vetsci12040301

A-6. HRV と内部状態
    • Katayama, Kubo, Mogi, Ikeda, Nagasawa, Kikusui, "Heart rate variability predicts the
      emotional state in dogs," Behavioural Processes 128:108-112, 2016．
      麻布大（菊水研）と奈良先端大（池田研）の共同．健康な家庭犬 33 頭．
      ネガティブ場面で RMSSD が低下，ポジティブ場面で SDNN が低下
      https://doi.org/10.1016/j.beproc.2016.04.015
    • "Beyond Cortisol! Physiological Indicators of Welfare for Dogs: Deficits,
      Misunderstandings and Opportunities," JAAWS, 2025．
      指標の構成概念妥当性（本当に福祉を測れているか）とイヌ固有の検証不足を指摘
      https://doi.org/10.1080/10888705.2025.2572616

A-7. 動物用ウェアラブルの設計
    • "Towards Effective Wearable Design: 20 Key Factors for Monitoring Physiological Health
      in Animals," 2025．動物側の特性への適応不足，計測手法の限界，使用条件の記録が
      標準化されていないことを指摘
      https://www.sciencedirect.com/science/article/pii/S2590123025020730
    • Foster, Brugarolas, Walker, Bozkurt ら, "Wearable and embedded sensor systems for
      animal welfare monitoring," ACI 2023
      https://doi.org/10.1145/3637882.3637899


付録 B. ミリ波で RR 間隔が取れるかの予備検討（公開ヒトデータ）

    なぜやったか
        • 非接触センサを足す案を相談する前に，取れる精度を自分の手で見積もっておきたかった
        • イヌのデータがまだ無いので，公開されているヒトのデータで試しました

    条件
        • データ：MMECG（Chen ら, IEEE Trans. Mobile Computing 23(1):270-285, 2024）
          ミリ波レーダと心電図の同時計測．公開分は 11 名・91 トライアル・約 4.6 時間
        • 分割：学習 7 名／検証 1 名／テスト 3 名．テストの人は学習に使っていない
        • 入力：レーダの反射信号（胸の 50 点，200 Hz，4 秒窓）
        • 出力：各時刻に R 波がある確からしさ．そこからピークを拾って RR 間隔にする

    結果（テスト 3 名・44 トライアル）
        • R 波の検出 F1：0.749
        • RR 間隔の平均絶対誤差：8.4 ms
        • RMSSD の誤差：10.3 ms
        • 参考：RR 間隔を報告している近縁研究（ICASSP 2024）が中央値 12 ms

    限界
        • ヒトの，横になっている条件での結果．イヌで成り立つ保証はない
        • データセット原著の信号処理コードが非公開のため，原著の報告値（3 ms）とは
          条件が違い，直接は比べられない
        • しきい値を下げても検出率は 0.83 で頭打ち．反応が出ていない拍は後処理では拾えない


付録 C. 評価で気をつけた点

    • 波形の相関は当てにならない
        ○ 心電図は個体差より P-QRS-T の共通の形が支配的
        ○ 入力を一切見ずに学習データの平均波形を出すだけのモデルでも相関 0.88 が出た
        ○ そのため相関を出すときは，この「平均波形モデル」の値を必ず並べて書くことにした
    • F1 も上げようと思えば上げられる
        ○ 正解に立てるガウシアンの幅を広げると，対応づけが緩くなって F1 だけ上がる
        ○ 位置精度（RR 誤差）は逆に悪化するので，F1 と RR 誤差は必ず一緒に見る
    • この 2 点は，イヌのデータで同じことをやるときにもそのまま効く注意点だと考えています
