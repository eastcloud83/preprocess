from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import MeCab
import glob
import pandas as pd
import statistics


def tokenize(docs_list):
    # type: (list) -> list
    """
    リスト内の文の単語を原形にして分かち書きをする関数
    :param docs_list:文が要素であるリスト
    :return: 分かち書きの文が要素であるリスト
    """
    m = MeCab.Tagger()
    wakati_docs_list = []
    for doc in docs_list:
        wakati_line = ""
        morph_info = m.parse(doc.replace("　", ""))  # 形態素解析, 全角の空白は取り除く
        for q_morph in morph_info.split("\n"):
            if (q_morph != "EOS") and (q_morph != ''):
                info = q_morph.split("\t")[1]  # 形態素情報
                word = info.split(",")[6]  # 単語の原形
                pos = info.split(",")[0]  # 品詞
                if word != "*":
                    if info.split(",")[1] != "非自立":
                        if pos == "名詞" or pos == "形容詞" or pos == "動詞" or pos == "副詞":
                            wakati_line = wakati_line + word + " "
        wakati_docs_list.append(wakati_line.rstrip(" "))
    return wakati_docs_list

# ディレクトリごとにファイルを読み込む
docs = []
tags = []
tag_id = 0
dirs = glob.glob("../../inamori_data_kai/*")  # 指定したディレクトリにあるすべてのディレクトリの読み込み
for dir_name in dirs:
    files = glob.glob(dir_name + "/*.txt")  # ディレクトリの中のすべての文書ファイルの読み込み
    for file_name in files:
        with open(file_name, "r") as f:
            whole_str = f.read()
            if whole_str != "":
                docs.append(whole_str.split("|")[-1])
                tags.append(tag_id)
    tag_id += 1
"""
count_vectorizer = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')  # binary=False：頻度を考慮
bow = count_vectorizer.fit_transform(tokenize(docs))

print(tokenize(docs))

print(count_vectorizer.get_feature_names())
print(bow.toarray())
print(count_vectorizer.vocabulary_)

# コサイン類似度計算
score = cosine_similarity(bow.toarray(), bow.toarray())
print(score)
print(score[0][1])  # 0行目1列目

"""
# TF-IDF
tfidf_vectorizer = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')
tfidf = tfidf_vectorizer.fit_transform(tokenize(docs))

# コサイン類似度計算
score = cosine_similarity(tfidf.toarray(), tfidf.toarray())
pd_score = pd.DataFrame(score)
pd_score.index = tags
pd_score.columns = tags

for i in range(tag_id):
    scores_list = []
    same_dir_score_list = []
    pd_i_score = pd_score.loc[i]  # 同じディレクトリだけ取り出す
    for index, row in pd_i_score.iterrows():
        for column_name, item in row.iteritems():
            if 0.99 > float(item):
                # print(str(index) + ", " + str(column_name))
                if column_name == index:  # 同じディレクトリ内
                    same_dir_score_list.append(item)
                else:
                    scores_list.append(item)
    print(str(index) + "：")
    same_score = statistics.mean(same_dir_score_list)
    all_score = statistics.mean(scores_list)
    print("同じ：" + str(same_score))
    print("全体：" + str(all_score))
    print("差：　" + str(same_score - all_score))
    print("--------------------")
