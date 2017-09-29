#!/usr/bin/env python
print("何段ですか：",end="")
side = int(input())

for a in range(side) :
    for b in range(side) :
        print("*",end="")
    print("")
"""
正方形を描画
"""