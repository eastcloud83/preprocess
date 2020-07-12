# 連続して出現する単語をカウント（N-gramの単語と品詞を考慮したようなプログラム）
import re
import numpy as np
from collections import Counter
import MeCab
import matplotlib.pyplot as plt
import glob
from matplotlib.font_manager import FontProperties

mecab = MeCab.Tagger("-Ochasen")

# ストップワード
stop_words = ["〇", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "円", "0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", "*"]
directory_name = input("ディレクトリ名：")


# ファイルを読み込み１文ずつリストに格納する
sentences = []  # 一文ごとに格納
dirs = glob.glob("../../{}/*".format(directory_name))  # 指定したディレクトリにあるすべてのディレクトリの読み込み
for dir_name in dirs:
    for file_name in glob.glob(dir_name + "/*.txt"):  # ディレクトリの中のすべての文書ファイルの読み込み
        with open(file_name, "r") as f:
            whole_str = f.read()
            if whole_str != "":
                for sentence in (re.sub('。', '。\n', whole_str.split("|")[-1])).splitlines():
                    sentences.append(sentence)


# 隣同士で出現した単語をタプルにしてリストに追加
all_cont_kyoki_list = []
for s in sentences:
    cont_kyoki_list = []
    node = mecab.parseToNode(s)
    while node:
        pos = node.feature.split(",")[0]
        if pos == "名詞" or pos == "形容詞" or pos == "副詞":  # 特定の品詞と非自立以外
            if node.feature.split(",")[1] != "非自立":
                word = node.feature.split(",")[6]  # 原形
                if word != "*":
                    if word not in stop_words:
                        cont_kyoki_list.append(word)
                        node = node.next
                        continue
        elif len(cont_kyoki_list) >= 2:
            all_cont_kyoki_list.append(tuple(cont_kyoki_list))  # タプルにしてリストに追加
        cont_kyoki_list = []
        node = node.next


# ペアの出現頻度をカウント
word_pair_cnt_dic = Counter(all_cont_kyoki_list)


# 以下グラフ用
word_list = []
freq_list = []
for word_count_tuple in sorted(word_pair_cnt_dic.items(), key=lambda x: x[1], reverse=True)[:55]:  # 上位55件を表示
    cont_kyoki_words = ""
    for i in range(len(word_count_tuple[0])):
        cont_kyoki_words += word_count_tuple[0][i] + " - "
    word_list.append(cont_kyoki_words.rstrip(" - "))
    freq_list.append(word_count_tuple[1])

# 日本語フォント
fp = FontProperties(fname='/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf')

plt.subplots(1, 1, figsize=(12,8))


# ラベル設定
plt.title("連続している名詞、形容詞、副詞", fontproperties=fp)
plt.xlabel('文字列', fontproperties=fp)
plt.ylabel('出現頻度', fontproperties=fp)

# データプロット
plt.yticks(np.arange(0, 55), word_list, fontproperties=fp, fontsize=6)
plt.barh(np.arange(0, 55), np.array(freq_list), height=0.5)
plt.show()
