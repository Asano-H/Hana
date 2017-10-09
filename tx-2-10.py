#読み込んだ２つの整数値の比率を百分率(実数)で表示
print("２つの整数を入力してください")
print("整数Ｘ：",end="")
x = int(input())
print("整数Ｙ：",end="")
y = int(input())
print("ＸはＹの",float(x)/float(y)*100.0,"％です")