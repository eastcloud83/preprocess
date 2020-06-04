import MeCab

file_path = input("ファイルパス：")
out_file_path = input("分かち書きファイルパス：")


def surface_wakati(file):
    # type: (str) -> list
    """
    単純な分かち書きをする関数（単語は表層系）
    :param file:普通の文書のファイルパス
    :return: ファイル１行ずつの分かち書きが要素となっているリスト
    """
    t = MeCab.Tagger("-Owakati")
    with open(file) as f:
        # 全角の空白を取り除く, .rstrip(" \n"):最後の文字の後ろのスペースを取り除く
        wakati_texts_list = [t.parse(line.replace("　", "")).rstrip(" \n") + "\n" for line in f]
    wakati_texts_list[-1] = wakati_texts_list[-1].rstrip("\n")  # 末尾は改行を削除
    return wakati_texts_list


def base_wakati(file):
    # type: (str) -> list
    """
    単語を原形にして分かち書きをする関数
    :param file:普通の文書のファイルパス
    :return: ファイル１行ずつの分かち書きが要素となっているリスト
    """
    m = MeCab.Tagger()
    wakati_texts_list = []
    with open(file) as f:
        for line in f:
            wakati_line = ""
            morph_info = m.parse(line.replace("　", ""))  # 形態素解析, 全角の空白は取り除く
            for q_morph in morph_info.split("\n"):
                if (q_morph != "EOS") and (q_morph != ''):
                    info = q_morph.split("\t")[1]  # 形態素情報
                    word = info.split(",")[6]  # 単語の原形
                    wakati_line = wakati_line + word + " "
            wakati_texts_list.append(wakati_line.rstrip(" ") + "\n")
    wakati_texts_list[-1] = wakati_texts_list[-1].rstrip("\n")  # 末尾は改行を削除
    return wakati_texts_list


wakati_texts_list = surface_wakati(file_path)
# wakati_texts_list = base_wakati(file_path)

with open(out_file_path, "w") as f2:
    f2.writelines(wakati_texts_list)

