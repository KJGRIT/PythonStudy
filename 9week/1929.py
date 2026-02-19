import sys
input = sys.stdin.readline

m,n = map(int, input().split())

p = [1] * (n+1)
p[1] = 0
y = int(n ** 0.5)

for i in range(2, y+1):
    if p[i] == 1:
        for j in range(i+i, n+1, i):
            p[j] = 0

for i in range(m, n+1):
    if p[i] == 1:
        print(i)
