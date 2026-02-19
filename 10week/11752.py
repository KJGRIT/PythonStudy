import sys
sys.setrecursionlimit(10 ** 6)              # 재귀 깊이 제한을 늘려 DFS 깊은 탐색 시 오류 방지
input = sys.stdin.readline

# 1. 입력받기
n = int(input())                            # 트리의 노드 개수 입력
visited = [False] * (n+1)                   # 각 노드 방문 여부 체크 배열
tree = [[] for _ in range(n+1)]             # 인접 리스트(트리 구조 저장) 생성
answer = [0] * (n+1)                        # 각 노드의 부모 노드를 저장하는 배열

# 2. 인접 리스트로 트리 데이터 구현
for _ in range(1,n):
    n1, n2 = map(int, input().split())      # 연결된 두 노드 입력
    tree[n1].append(n2)                     # n1의 인접리스트에 n2 추가
    tree[n2].append(n1)                     # n2의 인접리스트에 n1 추가 (양방향 연결)

# 3. DFS 구현
def DFS(number):
    visited[number] = True                  # 현재 노드를 방문 처리
    for i in tree[number]:                  # 현재노드와 연결된 모든 노드 탐색
        if not visited[i]:                  # 방문하지 않았다면
            answer[i] = number              # i번 노드의 부모는 현재 노드 number
            DFS(i)                          # i번 노드로 재귀 DFS 진행

DFS(1)                                      # 루트 노드 1번부터 탐색 시작

# 4. 출력
for i in range(2, n+1):                     # 2번 노드부터 각 노드의
    print(answer[i])                        # 부모 출력
