import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

s = set()
res = [0] * m

for i in a:
    s.add(i)

for i in range(m):
    if b[i] in s:
        res[i] = 1
    else:
        res[i] = 0

print(*res, sep=' ')

