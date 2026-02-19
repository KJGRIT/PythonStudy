import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 1. 입력 받기,저장 리스트 생성
v,e = map(int,input().split())                          # v: 정점 수, e: 간선 수
k = int(input())                                        # 시작 정점 번호
distance = [sys.maxsize]*(v+1)                          # 각 노드까지 최소 거리 저장(초기값: 무한대)
visited = [False]*(v+1)                                 # 방문 여부 체크 배열
myList = [[] for _ in range(v+1)]                       # 인접 리스트(그래프) 초기화
q = PriorityQueue()                                     # 우선순위 큐 생성

# 2. 그래프 생성
for _ in range(e):
    u,v,w = map(int,input().split())                    # u → v 로 가는 가중치 w의 간선
    myList[u].append((v, w))                            # u 정점 리스트에 (도착지, 가중치) 저장

# 3. 다익스트라 수행
q.put((0,k))                                            # (거리, 시작노드) 형태로 우선순위 큐 삽입
distance[k] = 0                                         # 시작 노드까지 거리는 0

while q.qsize() > 0:                                    # 큐가 빌 때까지 반복
    current = q.get()                                   # 현재 가장 최소 비용의 노드 꺼내기(거리, 노드)
    c_v = current[1]                                    # c_v : 현재 선택된 노드 번호
    if visited[c_v]:                                    # 이미 방문한 노드라면
        continue                                        # 스킵
    visited[c_v] = True                                 # 현재 노드 방문 처리
    for tmp in myList[c_v]:                             # 현재 노드와 연결된 모든 간선 탐색
        next = tmp[0]                                   # next : 다음에 이동할 노드 번호
        value = tmp[1]                                  # value : 현재 노드 → next 노드로 가능 가중치
        # 현재까지 온 거리 + 간선 가중치 < 기존에 저장된 next까지의 최단거리라면 갱신
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value      # 최단 거리 갱신
            q.put((distance[next], next))               # 갱신된 경로를 큐에 삽입하여 탐색 계속

# 4. 출력
for i in range(1, v+1):                                 # 1번 노드부터 v번 노드까지 출력
    if visited[i]:                                      # 방문한 적이 있다면
        print(distance[i])                              # 최단 거리 출력
    else:                                               # 방문한 적이 없다 = 최단 경로가 없음
        print("INF")                                    # INF 출력