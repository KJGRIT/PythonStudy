import sys
from queue import PriorityQueue
input = sys.stdin.readline

# 1. 입력받기
n,m = map(int,input().split())                  # n: 정점 수, m: 간선 수
pq = PriorityQueue()                            # 간선을 가중치 기준으로 오름차순 정렬하기 위한 우선순위 큐
parent = [0] * (n+1)                            # 유니온 파인드에서 각 정점의 부모를 저장할 배열

# 2. 유니온 파인드 초기화
for i in range(n+1):
    parent[i] = i                               # 처음에는 모든 노드의 부모가 자기 자신

for i in range(m):                              # m개의 간선
    s,e,w = map(int,input().split())            # 시작점, 도착점, 가중치 입력 받기
    pq.put((w,s,e))                             # pq에는 (가중치, 시작점, 도착점) 순으로 저장 → 자동으로 가중치 기준 정렬됨

def find(a):                                    # find함수 : 부모 노드를 찾고, 경로 압축 적용
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])             # 재귀적으로 최종 부모를 찾은 뒤, 저장하여 경로 단축
        return parent[a]

def union(a,b):                                 # Union함수 : 두 노드의 루트를 합치기
    a = find(a)
    b = find(b)
    if a != b:                                  # 값이 다르다면
        parent[b] = a                           # 한쪽 루트가 다른 쪽을 부모로 설정(합치기)

# 3. 크루스칼 알고리즘(MST 구성)
useEdge = 0                                     # 현재까지 사용한 간선 수 초기화
result = 0                                      # 가중치 합 초기화

while useEdge < n-1:                            # MST는 간선이 n-1개 선택되면 완성됨
    w,s,e = pq.get()                            # 가장 가중치가 작은 간선 꺼내기
    if find(s) != find(e):                      # 사이클이 발생하지 않은 경우만 사용
        union(s,e)                              # 두 정점을 하나의 집합으로 합치기
        result += w                             # 가중치 누적
        useEdge += 1                            # 사용한 간선 수 증가

# 4. 출력
print(result)                                   # 결과 출력