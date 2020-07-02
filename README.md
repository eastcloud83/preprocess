# preprocess
文章データの前処理用のプログラム（日本語用）
## Description
1. `wakatigaki_mecab.py` MeCabで文を分かち書きする
2. `vocab.py` 単語の分散表現のファイルから単語だけを抜き出す
3. `vocab_to_id.py` 分かち書きをID化する(1, 2で出力されたファイルを使用)

`cos_sim.py` 文同士のコサイン類似度を計算する

`sentence_split.py` 一文ずつで改行したファイルを作成

`text_mining` 出現頻度をグラフ表示する
