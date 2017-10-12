#読み込んだ２つの値の差が１０以下か判定
print("２つの整数を入力してください")
print("整数Ａ：",end="")
a = int(input())
print("整数Ｂ：",end="")
b = int(input())
sa = a-b
if sa>10 or sa<-10:
    print("それらの差は１１以上です")
else :
    print("それらの差は１０以下です")