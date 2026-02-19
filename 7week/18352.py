import sys
from collections import deque
input = sys.stdin.readline

#1. 입력 및 초기화
n,m,k,x = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
res = []

#3. BFS 함수 선언
def BFS(v):
    que = deque()
    que.append(v)
    visited[v] += 1
    while que:
        now_node = que.popleft()
        for i in A[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                que.append(i)
                
#2. 그래프 생성
for _ in range(m):
    s,e = map(int, input().split())
    A[s].append(e)
    
BFS(x)

#4. 출력
for i in range(n+1):
    if visited[i] == k:
        res.append(i)
        
if not res:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)