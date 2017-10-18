#読み込んだ整数値を１までカウントダウン
print("整数を入力してください：",end="")
no = int(input())
if no>=1:
    while no>=1:
        no=no-1
        print(no)
    print(" ")