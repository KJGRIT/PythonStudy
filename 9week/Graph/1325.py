import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())             # n = 컴퓨터의 개수, m = 신뢰 관계 수
A = [[] for i in range(n+1)]                # A[x] = x가 신뢰하는 컴퓨터 목록(그래프 인접 리스트)
answer = [0] * (n+1)                        # answer[i] = i번 컴퓨터가 해킹될 수 있는 횟수(= 다른 노드에서 BFS 돌렸을 때 도달되는 수)

def BFS(v):                                 # BFS 함수 정의
    visited = [False] * (n+1)               # 방문 여부 체크 배열
    que = deque()                           #
    que.append(v)                           # BFS 시작 노드 큐에 넣기
    visited[v] = True                       # 시작 노드 방문 처리
    while que:                              # 큐가 빌 때까지
        Now_node = que.popleft()            # 현재 탐색할 노드
        for i in A[Now_node]:               # 현재 노드에서 이동 가능한 노드 탐색
            if not visited[i]:              # 아직 방문하지 않았다면
                visited[i] = True           # 방문 처리
                answer[i] += 1              # i번 컴퓨터가 해킹될 수 있다는 의미로 count 증가
                que.append(i)               # 계속해서 탐색 진행

for i in range(m):                          # m개의 신뢰관계 입력(s가 e를 신뢰한다 = s를 해킹하면 e도 해킹 가능)
    s,e = map(int, input().split())
    A[s].append(e)                          # 그래프 생성

for i in range(1, n+1):                     # 모든 컴퓨터를 시작점으로
    BFS(i)                                  # BFS 실행

maxVal = max(answer)                        # 가장 많이 해킹 가능한 컴퓨터 수 찾기
for i in range(1, n+1):                     # 가장 많이 해킬될 수 있는 컴퓨터 번호 출력
    if maxVal == answer[i]:
        print(i, end=' ')


