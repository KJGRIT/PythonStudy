import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    x,y = map(int,input().split())
    a.append((x,y))

a.sort()

# for i in range(n):
#     x,y = a[i]
#     print(x,y)

for x,y in a:
    print(x,y)
