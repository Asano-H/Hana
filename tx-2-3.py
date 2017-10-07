#読み込んだ2つの値の比率を百分率で表示
print("整数を入力してください")
print("整数１：",end="")
a = int(input())
print("整数２：",end="")
b = int(input())
print("整数１は整数２の",int(100*a/b),"%です")