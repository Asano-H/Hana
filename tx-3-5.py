#読み込んだ二つの値の大小関係
print("２つの整数を入力してください")
print("整数Ａ：",end="")
a = int(input())
print("整数Ｂ：",end="")
b = int(input())
if a==b:
    print("ＡとＢは等しいです")
elif a>b:
	print("ＡはＢより大きいです")
else
    print("ＡはＢより小さいです")
