import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a=list(range(1,n+1))

for i in range(m):
    k,j = map(int, input().split())
    a[k-1], a[j-1] = a[j-1], a[k-1]
print(*a)
    
