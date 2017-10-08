#読み込んだ身長と体重からＢＭＩを求めて表示
print("身長を入力してください(cm)")
height = float(input())
print("体重を入力してください(kg)")
weight = float(input())
print("ＢＭＩは",weight/((height/100.0)*(height/100.0)),"です")