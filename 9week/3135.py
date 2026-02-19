import sys
input = sys.stdin.readline

a,b = map(int, input().split())
n = int(input())
res1 = abs(a-b)

for i in range(n):
    hz = int(input())
    res2 = abs(hz - b) + 1
    res1 = min(res1, res2)

print(res1)