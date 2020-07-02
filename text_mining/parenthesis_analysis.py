# 鍵括弧の内容をカウント
import glob
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import re

directory_name = input("ディレクトリ名：")

# ディレクトリごとにファイルを読み込む
dirs = glob.glob("../../{}/*".format(directory_name))  # 指定したディレクトリにあるすべてのディレクトリの読み込み

words = []
for dir_name in dirs:
    files = glob.glob(dir_name + "/*.txt")  # ディレクトリの中のすべての文書ファイルの読み込み
    # このプログラムで使用するファイルを選んでリストにファイル名を格納
    for file_name in files:
        with open(file_name) as f:
            text = f.read()
            for sentence in re.findall(r"\「(.+?)\」", text):
                words.append(sentence)
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


# ラベル設定
plt.title("カッコ内の文字列", fontproperties=fp)
plt.xlabel('文字列', fontproperties=fp)
plt.ylabel('出現頻度', fontproperties=fp)

# データプロット
plt.yticks(np.arange(0, 50), word_list, fontproperties=fp, fontsize=6)
plt.barh(np.arange(0, 50), np.array(freq_list), height=0.5)
plt.show()
