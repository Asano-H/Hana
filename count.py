import time
count_limit= int(input())

while count_limit >= 0:
    if count_limit == 0:
        print("Over")
    else:
        print(count_limit)
    count_limit -= 1
    time.sleep(1)

