import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = [[0] for _ in range(n+1)]

for _ in range(n):
    Data = list(map(int, input().split()))
    index = 0
    s = Data[index]
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index + 1]
        a[s].append((E,V))
        index += 2
        
distance = [0] * (n+1)
visited = [False] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True 
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True 
                queue.append(i[0])
                distance[i[0]] = ditance[now_node] + i[1]
                
BFS(1)
max = 1
for i in range(2, n+1):
    if distance[max] < distance[i]:
        max = i
        
distance = [0] * (n+1)
visited = [False] * (n+1)

BFS(max)
distance.sort()
print(distance[n])