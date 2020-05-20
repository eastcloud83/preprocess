import MeCab

t = MeCab.Tagger("-Owakati")

file_path = input("ファイルパス：")
out_file_path = input("分かち書きファイルパス：")

with open(file_path) as f:
    wakati_texts = [t.parse(line) for line in f]

with open(out_file_path, "w") as f2:
    f2.writelines(wakati_texts)
