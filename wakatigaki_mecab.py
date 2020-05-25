import MeCab

t = MeCab.Tagger("-Owakati")

file_path = input("ファイルパス：")
out_file_path = input("分かち書きファイルパス：")

with open(file_path) as f:
    wakati_texts_list = [t.parse(line).rstrip(" \n") + "\n" for line in f]  # .rstrip(" \n"):最後の文字の後ろのスペースを取り除く

wakati_texts_list[-1] = wakati_texts_list[-1].rstrip("\n")  # 末尾は改行を削除

with open(out_file_path, "w") as f2:
    f2.writelines(wakati_texts_list)

