vocab_file_path = input("分散表現から抜き出した単語のファイルパス：")  # 入力１
wakati_file_path = input("分かち書きファイルパス：")  # 入力２
wakati_id_file_path = input("ID化した分かち書きファイルパス：")  # 出力

# 単語をリストに追加
with open(vocab_file_path) as f:
    vocab_list = [vocab.rstrip("\n") for vocab in f]

# 分かち書きファイルをID化
wakati_id_str = ""
with open(wakati_file_path) as f2:
    for wakati_line in f2:
        wakati_line = wakati_line.rstrip("\n")
        for wakati_vocab in wakati_line.split(" "):
            if wakati_vocab in vocab_list:  # 単語がリストにある
                vocab_id = vocab_list.index(wakati_vocab)
            else:  # 単語がリストにない
                if wakati_vocab == " ":
                    vocab_id = 0
                else:
                    vocab_id = 1
            wakati_id_str += str(vocab_id) + " "
        wakati_id_str = wakati_id_str.rstrip(" ") + "\n"

with open(wakati_id_file_path, "w") as f3:
    f3.write(wakati_id_str.rstrip("\n"))