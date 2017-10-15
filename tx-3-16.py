#読み込んだ月の季節を表示
print("何月ですか：",end="")
month = int(input())

if 3<=month or month<=5:
    print("春")
elif 6<=month or month<=8:
    print("夏")
elif 9<=month or month<=11:
    print("秋")
elif month<=2 or month==12:
    print("冬")