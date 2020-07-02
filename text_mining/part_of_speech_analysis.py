# 指定された品詞の単語をカウント
import MeCab
import glob
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

num = input("品詞の数字を選択してください（1:名詞, 2:動詞, 3:形容詞, 4:副詞）：")
pos_dic = {"1": "名詞", "2": "動詞", "3": "形容詞", "4": "副詞"}
pos = pos_dic[num]

shape = input("形の数字を入力してください(0:表層形, 1:原形)：")

directory_name = input("ディレクトリ名：")

mecab = MeCab.Tagger("-Ochasen")

# ディレクトリごとにファイルを読み込む
dirs = glob.glob("../../{}/*".format(directory_name))  # 指定したディレクトリにあるすべてのディレクトリの読み込み

words = []
for dir_name in dirs:
    files = glob.glob(dir_name + "/*.txt")  # ディレクトリの中のすべての文書ファイルの読み込み
    # このプログラムで使用するファイルを選んでリストにファイル名を格納
    for file_name in files:
        with open(file_name) as f:
            text = f.read()
            # 形態素解析
            node = mecab.parseToNode(text)
            while node:
                if node.feature.split(",")[0] == pos and node.feature.split(",")[1] != "非自立":  # 選択された品詞の非自立以外を追加
                    if shape == "0":
                        words.append(node.surface)  # 表層形を追加
                    elif shape == "1":
                        words.append(node.feature.split(",")[6])  # 原形を追加
                node = node.next

p_words = list(set(words))  # words内の重複要素を削除

word_count_list = []
for word in p_words:
    word_count_list.append((word, words.count(word)))
word_count_list = sorted(word_count_list, key=lambda x: x[1], reverse=True)
word_list = []
freq_list = []
for word_count_tuple in word_count_list[:50]:  # 上位50件を表示
    word_list.append(word_count_tuple[0])
    freq_list.append(word_count_tuple[1])
    print(word_count_tuple)

# 日本語フォント
fp = FontProperties(fname='/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf')

plt.subplots(1, 1, figsize=(12,8))

if shape == "0":
    shape = "表層形"
elif shape == "1":
    shape = "原形"


# ラベル設定
plt.title(pos + ", " + shape + ", 非自立なし", fontproperties=fp)
plt.xlabel('単語', fontproperties=fp)
plt.ylabel('出現頻度', fontproperties=fp)

# データプロット
plt.yticks(np.arange(0, 50), word_list, fontproperties=fp, fontsize=6)
plt.barh(np.arange(0, 50), np.array(freq_list), height=0.5)
plt.show()
