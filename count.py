import time
count_limit= int(input()) #カウントする秒数を入力する

while count_limit >= 0:
    if count_limit == 0:
        print("Go")
    else:
        print(count_limit) #カウントを画面に出力する
    count_limit -= 1 #カウントをデクリメント
    time.sleep(1) #1秒待つ

"""
1秒ずつカウントダウンする
"""