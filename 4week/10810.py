import sys
input = sys.stdin.readline

N,M = map(int, input().split())
a = [0]*N

for x in range(M):
    i,j,k = map(int, input().split())
    for idx in range(i-1,j):
        a[idx] = k
print(*a)