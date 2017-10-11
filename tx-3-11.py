#読み込んだ３つの値の等値関係
print("３つの整数を入力してください")
print("整数１：",end="")
a = int(input())
print("整数２：",end="")
b = int(input())
print("整数３：",end="")
c = int(input())
if a==b and b==c:
    print("３つの値は等しいです")
elif a==b or b==c or c==d:
    print("２つの値は等しいです")
else :
    print("３つの値は異なります") 