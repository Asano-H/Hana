import time
print("何秒ですか")
count_limit = int(input())

for a in range(count_limit+1) :
	if count_limit==a:
		print("Go")
	else:
		print(count_limit-a)
	time.sleep(1)