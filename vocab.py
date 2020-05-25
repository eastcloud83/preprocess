# 分散表現が書かれたファイル
vocab_file_path = input("単語分散表現ファイルパス：")

vocab_list = ["_PAD" + "\n", "_UNK" + "\n"]  # 単語を格納するリスト

flag = False  # 1行目は追加しない(形式の記述があるから)
with open(vocab_file_path) as vf:
    for vocab_line in vf:
        if flag:
            vocab_list.append(vocab_line.split(" ")[0] + "\n")
        flag = True

vocab_list[-1] = vocab_list[-1].rstrip("\n")  # 末尾の単語は改行を削除

with open("vocab.txt", 'w') as f:
    f.writelines(vocab_list)
