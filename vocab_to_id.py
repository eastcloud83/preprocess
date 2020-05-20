vocab_file_path = input("単語ファイルパス：")
wakati_file_path = input("分かち書きファイルパス：")
wakati_id_file_path = input("ID化した分かち書きファイルパス：")

# 単語ファイルの単語をリストに追加
vocab_list = []
with open(vocab_file_path) as f:
    for vocab in f:
        vocab_list.append(vocab.rstrip("\n"))

# 分かち書きファイルをID化
wakati_id_str = ""
with open(wakati_file_path) as f2:
    for wakati_line in f2:
        wakati_line = wakati_line.rstrip("\n")
        for wakati_vocab in wakati_line.split(" ")[:-1]:
            if wakati_vocab in vocab_list:
                vocab_id = vocab_list.index(wakati_vocab)
            else:
                if wakati_vocab == " ":
                    vocab_id = 0
                else:
                    vocab_id = 1
            wakati_id_str += str(vocab_id) + " "
        wakati_id_str += "\n"

with open(wakati_id_file_path, "w") as f3:
    f3.write(wakati_id_str.rstrip("\n"))
            
