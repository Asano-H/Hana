#読み込んだ値の符号を判定
print("整数を入力してください：",end="")
no = int(input())
if no == 0:
    print("その数は０です")
elif no>0:
    print("その数は正です")
elif no<0:
    print("その数は負です")