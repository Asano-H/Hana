s="abcd123"	#元の文字列

str_list=list(s)	#リストにする
print(str_list)

str_list[4]="e"	#リストの４番目の要素をeに変更する

str_change="".join(str_list)

print(str_change)

"""
文字列は変更することができない
文字列をばらして一度リストに変換することで編集可能となる
"""