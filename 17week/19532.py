import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())
res = []

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            res = [x,y]
            break
    if len(res) > 0:
        break
