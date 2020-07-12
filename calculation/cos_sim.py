from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import MeCab


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
                wakati_line = wakati_line + word + " "
        wakati_docs_list.append(wakati_line.rstrip(" "))
    return wakati_docs_list


docs = ["あなたにお聞きしたいのですが、今日の天気はどうですか。", "今日はいい天気です。今日は公園に行きましょう。"]
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
print(tfidf.toarray())
print(tfidf_vectorizer.vocabulary_)

# コサイン類似度計算
score = cosine_similarity(tfidf.toarray(), tfidf.toarray())
print(score)
print(score[0][1])  # 0行目1列目
"""

