import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        return gcd(b, a%b)
    return a 

a,b = map(int, input().split())
res = gcd(a,b)

while res > 0:
    print(1, end='')
    res -= 1