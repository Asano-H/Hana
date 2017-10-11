#読み込んだ２つの整数値の差
print("２つの整数を入力してください")
print("整数Ａ：",end="")
a = int(input())
print("整数Ｂ：",end="")
b = int(input())
if a>b:
    sa = a-b
else :
    sa = b-a
print("２つの値の差は",sa,"です")