#読み込んだ値から台形の面積を求めて表示
print("台形の面積を求めます。数値を入力してください")
print("上辺：",end="")
a = int(input())
print("下辺：",end="")
b = int(input())
print("高さ：",end="")
c = int(input())
print("面積は",(a+b)*c/2.0,"です")