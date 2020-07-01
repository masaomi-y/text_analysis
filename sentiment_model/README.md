# Twitterネガポジ判断モデル作成・適用
下記ソースをベースに作成。
　https://qiita.com/ysiny/items/b01250228e0c5cc0e647
　https://github.com/sinjorjob/chABSA-dataset

## ディレクトリ構成

├─data
│  └─Twitter日本語評判分析データセット.txt
│  └─test.tsv    				#テスト用データ
│  └─train.tsv   	 			#訓練用データ
│  └─test_dumy.tsv  				#ダミーデータ
│  └─train_dumy.tsv 				#ダミーデータ

├─utils
│  └─bert.py    				#BERTモデルの定義
│  └─config.py  				#各種パスの定義
│  └─dataloader.py    			#dataloader生成用
│  └─predict.py    				#推論用
│  └─predict.py    				#推論用
│  └─tokenizer.py   				#形態素解析用
│  └─train.py       				#学習用 
├─vocab      					# bert語録辞書vocab.txt　　　　　　　 … ※1
└─weights    					# bert_config.json、pytorch_model.bin … ※1
└─Twitter学習データの作成.ipynb   		#tsvデータ作成
└─Twitterネガポジモデル作成・適用.ipynb   	#データローダ作成~学習~推論

※1：下記HPからダウンロードして配置
     https://alaginrc.nict.go.jp/nict-bert/index.html
     NICT_BERT-base_JapaneseWikipedia_32K_BPE.zipをダウンロード