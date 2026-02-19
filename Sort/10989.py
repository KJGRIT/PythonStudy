import sys
input = sys.stdin.readline

n = int(input())
a = [0] * 10001

for _ in range(n):
    x = int(input())
    a[x] += 1

for i in range(1,10001):
    for j in range(a[i]):
        print(i)