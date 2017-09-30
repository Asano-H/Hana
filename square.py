#!/usr/bin/env python
def main():
    print("何段ですか：",end="")
    side = int(input())

    for a in range(side) :
        for b in range(side) :
            print("＊",end="")
        print("")

if __name__=="__main__":
	main()
"""
正方形を描画
"""