#読み込んだ値の符号を判定
while True:
    print("整数を入力してください：",end="")
    num = int(input())
    if num==0:
        print("その数は０です")
    elif num>0:
        print("その数は正です")
    else :
        print("その数は負です")

    print("もう一度？【Yes・・・０/No・・・９】：")
    retry = int(input())
    if retry ==9:
        break
    

