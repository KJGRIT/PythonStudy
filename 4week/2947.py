import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
for i in range(5):
    for j in range(4):
        if a[j+1]<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
            print(*a)