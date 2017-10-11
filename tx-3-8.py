#４つの値を読み込んで最大値を表示
print("４つの整数を入力してください")
data = [int(input()) for i in range(4)]
print("最大値は",max(data),"です")