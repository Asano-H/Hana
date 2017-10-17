#読み込んだ整数値を０までカウントダウン
print("正の整数を入力してください")
no = int(input())
if no>=0:
    while no>=0:
        print(,no,end="")
        no--
    print("")