import glob
import os

for dir_name in glob.glob("../data_kai/*"):  # すべてのディレクトリの読み込み
    for file_name in glob.glob(dir_name + "/*.txt"):  # ディレクトリの中のすべての文書ファイルの読み込み
        with open(file_name) as f:
            txt = f.read()
            txt2 = txt.split("|")[-1]  # タイトルの部分を削除
            split_txt = "。\n".join(txt2.split("。"))  # 文で改行
        # 出力するファイルのパスを作成
        file_path_list = file_name.split("/")
        out_file_path = file_name.replace(file_path_list[-2], file_path_list[-2]+"_split")
        out_dir_path = "/".join(out_file_path.split("/")[:-1])
        if not os.path.exists(out_dir_path):
            os.mkdir(out_dir_path)
        # 書き込み
        with open(out_file_path, "w") as f2:
            f2.write(split_txt)
