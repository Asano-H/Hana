print("整数を入力してください：",end="")
inp=int(input())
i=1
while i<=inp:
	j=1
	k=1
	while j<=inp-i:
		print(" ",end="")
		j=j+1
	while k<=i*2-1:
		print("*",end="")
		k=k+1
	print(" ")
	i=i+1

"""
入力された段数のピラミッドを作成するプログラム
"""