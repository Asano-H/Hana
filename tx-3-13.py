#読み込んだ点数の判定して表示
print("点数：",end="")
point = int(input())
if point<0 or point>100:
    print("不正な結果です")
elif point<60:
    print("不可")
elif point<70:
    print("可")
elif point<80:
    print("良")
else :
    print("優")