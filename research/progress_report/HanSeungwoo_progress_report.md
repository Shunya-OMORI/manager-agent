
	• ECG再合成

1. グラフモデル構築のための資料調査

	• それぞれの長所, 短所がある
	• Graph transformerベースモデルを構築する
		○ 拡散モデルより軽いものを作りたい計画
		○ 従来の研究より結果が良くなければ
			▪ 強化学習でモデルパラメータを検索/最適化する計画
			▪ 最適化はモデルの大きさや精度
	
	2. SCG/GCGのデータ（安定時）ダウンロード
	• ‘Mechanocardiograms with ECG Reference’’ Dataset
			▪ https://ieee-dataport.org/documents/mechanocardiograms-ecg-reference
	• 29名 (3~10min)

	• HRV予測
	
	1. ヒトのACCからの心拍予測に関する資料調査
		a. イヌ実験のIMU軸(6軸*4個=24個)
	2. 転移学習でヒトのHR予測モデルからイヌのデータに適用
	3. HRではなくHRV全部を予測することは資料調査中


ヒトのACCからの心拍予測に関する資料調査



論文	入力	データセット	結果 	モデル
			(Avg. MAE)
Aguiar+, Brazilian Conference on Intelligent Systems, 2021	ACC (Wrist), ACC (Chest)	PAMAP2 (8名),	PAMAP2: 11.5	CNN-LSTM
		PPG-DaLiA(15名),	PPG-DaLiA: 13.5
		
Song+, IEEE SENSORS JOURNAL, 2021	PPG, ACC (Wrist)	PPG-DaLiA,	PPG-DaLiA : 6.02	CNN-LSTM (Neural architecture search)
		IEEE Signal Processing Cup 2015 dataset (TROIKA) (12名)	TROIKA:0.82
		BAMI (48名)	
			
Zhao+, IEEE SENSORS JOURNAL, 2021	ACC (Wrist)	Inhouse dataset 	3.70	Signal processing
		(20名)		(Singular spectrum analysis)
Romano+, MDPI Biosensors, 2022	ACC (Chest),	Inhouse dataset 	MAEは無い	Signal processing
	Gyro (Chest)	(11名)		
			1. ウィンドウの長さは精度に影響	各ウィンドウのPower Spectral Density (PSD)から計算

				HR= MaxPSD * 60 
			2. 座っていたり横になっていたりする時は推定精度が良い	[refが MDPI Sensors, そしてrPPG]
			
			3. 立っている姿勢では低下
TALUKDAR+ IEEE Access, 2022	PPG, ACC (Wrist)	TROIKA (12名)	0.92	Signal processing
				(Frequency analysis)
Ribeiro+, IEEE International Conference on Bioinformatics and Biomedicine	-	PPG-DaLiA	-	AI
(BIBM), 2023				(ろんぶんのタイトルが
				AI-based models to predict the heart rate using PPG and accelerometer signals during physical exercise)
Moebus+, IEEE J. BIOMEDICAL AND HEALTH INFORMATICS, 2025	ACC (Wrist)	Nightbeat-DB 	0.88	Signal processing
		(42名)		
				(STFT -> Frequency analysis)
