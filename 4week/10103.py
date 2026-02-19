import sys
input = sys.stdin.readline

a = int(input())
res1 = 100
res2 = 100

for i in range(a):
    b,c = map(int, input().split())
    
    if b < c:
        res1 -= c
    elif b > c:
        res2 -= b

print(res1)
print(res2)
