#読み込んだ整数値ＸはＹの約数か
print("２つの整数を入力してください")
print("Ｘ")
x = int(input())
print("Ｙ")
y = int(input())
if x%y:
    print("ＹはＸの約数ではありません")
else
    print("ＹはＸの約数です")
