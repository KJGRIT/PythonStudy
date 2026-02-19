import sys
sys.setrecursionlimit(10 ** 6)                  # 재귀 깊이 제한 증가(DFS에서 깊은 탐색이 필요할 수 있어 설정)
input = sys.stdin.readline

n = int(input())                                # 테스트 케이스 개수 입력
IsEven = True                                   # 이분 그래프 여부를 저장할 변수(True면 이분 그래프 가능)

def DFS(node):
    global IsEven                               # DFS를 통해 그래프를 탐색하면서 각 노드의 그룹(짝/홀)을 체크
    visited[node] = True                        # 현재 노드를 방문 처리
    for i in A[node]:                           # 현재 노드와 연결된 모든 이웃 노드 확인
        if not visited[i]:                      # 방문하지 않은 노드라면
            check[i] = (check[node] +1) % 2     # 부모 노드와 다른 그룹(0→1, 1→0)으로 설정
            DFS(i)                              # 재귀적으로 방문
        elif check[node] == check[i]:           # 이미 방문한 노드인데 그룹이 같다면
            IsEven = False                      # 이분 그래프 불가능

for _ in range(n):                              # n개의 테스트 케이스 처리
    v,e = map(int,input().split())              # v: 정점 수, e: 간선 수
    A = [[] for _ in range(v+1)]                # 인접 리스트 초기화
    visited = [False] * (v+1)                   # 방문 여부 저장 배열
    check = [0] * (v+1)                         # 각 노드의 그룹(0 또는 1) 저장
    IsEven = True                               # 초기값은 이분 그래프 가능(True)

for i in range(e):                              # 간선 정보 입력 (그래프 생성)
    start, end = map(int,input().split())       #
    A[start].append(end)                        # 양방향 연결
    A[end].append(start)

for i in range(1,v+1):                          # 정점 1부터 v까지 DFS 수행
    if IsEven:                                  # 아직 이분 그래프 가능성이 있으면
        DFS(i)                                  # DFS 수행
    else:                                       # 이미 불가능하다고 판정되면
        break                                   # 종료

if IsEven:                                      # 결과 출력, True면 이분 그래프
    print("YES")
else:
    print("NO")


