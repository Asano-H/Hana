#読み込んだ整数の絶対値を表示
print("整数を入力してください：")
no = int(input())
if no<0:
    no = -no
print("絶対値は",no,"です")