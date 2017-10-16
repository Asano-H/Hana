#読み込んだ値の、小さい数から大きい数までの和
print("２つの整数を入力してください")
print("整数Ａ：",end="")
a = int(input())
print("整数Ｂ：",end="")
b = int(input())
if a>b:
    low = b
    high = a
else :
    low = a
    high = b

no = low
num = 0
while True:
    num = num + no
    no = no + 1
    if high < no:
        break
print(low,"以上",high,"以下の整数の和は",num,"です")