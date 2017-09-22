a="abcabca"
print(a)

print(a.strip("a"))	#両端の削除

print(a.lstrip("a"))	#左端の削除

print(a.rstrip("a"))	#右端の削除

print("    abc".strip())	#空白を削除

"""
strip関数
.strip(削除したい文字列)
厳密には、削除ではなく特定の文字を取り除いた新しい文字列を返す処理
削除する文字列を指定しない場合、空白を削除

"""