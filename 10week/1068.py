import sys
sys.setrecursionlimit(10**6)                            # DFS 깊이 제한 늘리기(재귀 오류 방지)
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())                                        # 트리의 노드 개수
visited = [False] * (n)                                 # 각 노드 방문 여부 체크
tree = [[] for _ in range(n)]                           # 인접 리스트(트리 구조 저장)
answer = 0                                              # 삭제 후 남는 리프 노드 개수
p = list(map(int, input().split()))                     # 각 노드의 방문 정보

# 2. 인접 리스트에 트리 데이터 구현
for i in range(n):
    if p[i] != -1:                                      # 부모가 존재하면
        tree[i].append(p[i])                            # i → 부모 연결
        tree[p[i]].append(i)                            # 부모 → i 연결 (양방향 연결)
    else:
        root = i                                        # 부모가 -1이면 해당 노드가 루트 노드

# 3. DFS 구현
def DFS(number):
    global answer
    visited[number] = True                              # 현재 노드 방문 처리
    cNode = 0                                           # 자식 노드 수(삭제된 노드는 자식에서 제외)
    for i in tree[number]:                              # 현재 노드에 연결된 모든 노드 탐색
        if not visited[i] and i != deleteNode:          # 방문하지 않았고, 삭제 노드가 아니면
            cNode += 1                                  # 실제 존재하는 자식 노드 카운트
            DFS(i)                                      # 자식 노드 DFS 탐색
    if cNode == 0:                                      # 연결된 자식이 하나도 없으면
        answer += 1                                     # 리프 노드로 카운트

deleteNode = int(input())                               # 삭제할 노드 번호 입력

# 4. 출력
if deleteNode == root:                                  # 루트 자체가 삭제되면 트리가 사라짐
    print(0)                                            # 리프노드 0개
else:                                                   #
    DFS(root)                                           # 루트를 기준으로 DFS 돌며 리프 노드 세기
    print(answer)                                       # 남아있는 리프 노드 개수 출력