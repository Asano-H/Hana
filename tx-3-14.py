#読み込んだ値は等しいか
print("２つの整数を入力してください")
print("整数Ａ：",end="")
a = int(input())
print("整数Ｂ：",end="")
b = int(input())
if a==b:
    print("二つの値は同じです")
else :
    if a>b:
        mi = b
        ma = a
    else :
        mi = a
        ma = b
    print("大きい値は",ma,"です")
    print("小さい値は",mi,"です")