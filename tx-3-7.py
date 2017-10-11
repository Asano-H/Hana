#３つの値を読み込んで最小値を表示
print("３つの整数を入力してください")
data =[int(input()) for i in range(3)]
print("最小値は",min(data),"です")