import csv

csv_path = "source.csv"

def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    with open(csv_path, encoding="utf-8") as f:
      source = f.read().split('\n')

      if word in source: #wordの照合成功
        print(f"{word}が見つかりした")
      else: #wordの照合失敗
        print(f"{word}は見つかりませんでした")
        source.append(word)
        #書き込みモードでファイルを開く
        with open(csv_path, mode = "w", newline="", encoding="utf-8") as f:
          f.write("\n".join(source)) 


if __name__ == "__main__":
    search()
