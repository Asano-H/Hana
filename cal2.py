import math

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    p = pow(b,2)
    d =p-4*a*c
    e =math.sqrt(d)
    m =-b+e
    n =-b-e

    f=m/2*a
    g=n/2*a
    print(f,g)

if __name__=="__main__":
	main()