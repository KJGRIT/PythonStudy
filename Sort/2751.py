import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

a.sort()

for i in range(n):
    print(a[i])
