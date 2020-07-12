# preprocess
文章データの前処理用のプログラム（日本語用）
## Description
### `add_id`
文書を分かち書きして、id化するためのプログラム
1. `wakatigaki_mecab.py` MeCabで文を分かち書きする
2. `vocab.py` 単語の分散表現のファイルから単語だけを抜き出す
3. `vocab_to_id.py` 分かち書きをID化する(1, 2で出力されたファイルを使用)

- `sentence_split.py` 一文ずつで改行したファイルを作成

#### `calculation`
計算を行うプログラム
- `cos_sim.py` 文同士のコサイン類似度を計算する(出現頻度とTF・IDF)
- `file_cos_sim.py` 同じディレクトリ内のファイルとの類似度の平均と違うディレクトリのファイルとの類似度の平均の差を表示

#### `text_mining`
それぞれの方法で抽出した文字列の出現頻度をグラフで表示するプログラム
- `cont_kyoki_word.py` 繋がって出現する単語をカウントして表示
- `n_gram_analysis.py` N-gram
- `parenthesis_analysis.py` "「」"内の文字列
-  `part_of_speech_analysis.py` 指定した品詞
