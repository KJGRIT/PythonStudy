import sys
from collections import deque                       # 큐 자료구조를 사용하기 위해 deque 라이브러리 사용

input = sys.stdin.readline                          # 빠른 입력을 위해

# 1. 입력 받기 및 인접 리스트, 진입차수 리스트 생성
n,m  = map(int, input().split())                    # 노드의 개수 n과 간선의 개수 m을 입력 받기
A = [[] for _ in range(n+1)]                        # 그래프의 연결 관계를 저장할 인접 리스트 A를 생성
indegree = [0] * (n+1)                              # 각 노드의 진입 차수를 저장할 리스트 생성

# 2. 그래프 및 진입 차수 초기 데이터 저장
for i in range(m):                                  # 간선의 개수 m 만큼 반복
    s,e = map(int, input().split())                 # 시작 노드 s와 도착 노드 e를 입력 받기
    A[s].append(e)                                  # s → e 간선 인접 리스트에 저장
    indegree[e] += 1                                # 도착 노드 e의 진입 차수 1 증가

# 3. 위상 정렬 수행
que = deque()                                       # 위상정렬을 수행할 때 사용할 큐를 생성

for i in range(1,n+1):                              # 1번 노드부터 n번 노드까지 반복하면서
    if indegree[i] == 0:                            # 현재 노드 i의 진입 차수가 0이면
        que.append(i)                               # 큐에 해당 노드를 추가합니다

while que:                                          # 큐가 빌때까지 반복합니다.
    now = que.popleft()                             # 큐에서 현재 처리할 노드를 꺼냅니다
    print(now, end=' ')                             # 현재 노드를 위상 정렬 순서로 출력합니다
    for next in A[now]:                             # 현재 노드 now와 연결된 next 노드들을 순회합니다.
        indegree[next] -= 1                         # 다음 노드 next의 진입 차수를 1 감소시킵니다
        if indegree[next] == 0:                     # 진입 차수가 1 감소하여 0이 되었다면
            que.append(next)                        # 다음 노드 next를 큐에 추가합니다