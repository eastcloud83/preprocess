# 分散表現が書かれたファイル
vocab_file_path = input("単語分散表現ファイルパス：")

vocab_list = []
vocab_list.append("_PAD" + "\n")
vocab_list.append("_UNK" + "\n")  # 未知語

flag = False  # 1行目は追加しない
with open(vocab_file_path) as vf:
    for vocab_line in vf:
        if flag:
            vocab_list.append(vocab_line.split(" ")[0] + "\n")
        flag = True

vocab_list[-1] = vocab_list[-1].rstrip("\n")  # 最後の単語は改行コード削除

with open("vocab.txt", 'w') as f2:
    for vocab in vocab_list:
        f2.write(vocab)
