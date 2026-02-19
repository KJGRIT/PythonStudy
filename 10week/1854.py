import sys
import heapq
input = sys.stdin.readline

# 1. 입력받기, 거리 리스트를 제일 큰 값으로 초기화
n,m,k = map(int, input().split())                           # n : 노드 수, m : 간선 수, k : k번째 최단거리까지 저장하기 위한 값
w = [[] for _ in range(n+1)]                                # 인접 리스트 생성, 튜플 형태로 저장
distance = [[sys.maxsize] * k for _ in range(n+1)]          # 각 노드마다 k개의 거리 값을 저장하며, 처음엔 모두 무한대

# 2. 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())                       # a → b 가중치 c
    w[a].append((b,c))

# 3. 다익스트라 수행
pq = [(0,1)]                                                # (현재까지의 비용, 현재 노드)
distance[1][0] = 0                                          # 시작 노드의 첫번째 최단거리는 0으로 설정
while pq:                                                   # pq가 빌 때까지
    cost,node = heapq.heappop(pq)                           # 현재 가장 짧은 경로 꺼내기
    for nNode, nCost in w[node]:                            # 현재 노드에서 갈 수 있는 모든 다음 노드 탐색
        sCost = cost + nCost                                # node → nNode 로 갈 때의 총 비용
        if distance[nNode][k-1] > sCost:                    # nNode까지의 k번째 최단거리보다 더 짧다면 갱신
            distance[nNode][k-1] = sCost                    # k번째 값 위치에 새로운 값 삽입
            distance[nNode].sort()                          # 정렬하여 k개의 값이 항상 오름차순 유기
            heapq.heappush(pq, (sCost, nNode))         # 새 경로를 pq에 삽입

# 4. 출력
for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:                     # 도달하지 못한 경우
        print(-1)                                           # -1 출력
    else:
        print(distance[i][k-1])                             # k번째 최단거리 출력