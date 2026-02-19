import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
IsEven = True

def DFS(node):
    global IsEven
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            check[i] = (check[node] + 1) % 2
            DFS(i)
        elif check[node] == check[i]:
            IsEven = False

for _ in range(n):
    v,e = map(int,input().split())
    A = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    IsEven = True

for i in range(e):
    start,end = map(int,input().split())
    A[start].append(end)
    A[end].append(start)

for i in range(1,v+1):
    if IsEven:
        DFS(i)
    else:
        break
