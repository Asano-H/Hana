#読み込んだ整数以下の偶数を昇順に表示
print("正の整数を入力してください")
no = int(input())
if no>=1:
    i = 2
    while i<no:
        print(i)
        i=i+2