#読み込んだ整数値ＸはＹの約数か
print("２つの整数を入力してください")
print("Ｘ：",end="")
x = int(input())
print("Ｙ：",end="")
y = int(input())
if x%y:
    print("ＹはＸの約数ではありません")
else :
    print("ＹはＸの約数です")