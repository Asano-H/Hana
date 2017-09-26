print("何段にしますか？",end="")
inp=int(input())
i=1
while i<=inp:
	j=1
	k=1
	while j<=i-1:
		print(" ",end="")
		j=j+1
	while k<=(inp-i)*2+1:
		print("*",end="")
		k=k+1
	print("")
	i=i+1
"""
入力された数値の段数の逆ピラミッドを作成するプログラム
"""