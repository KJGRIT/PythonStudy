import sys
from collections import deque
input = sys.stdin.readline

# 1. 입력 받기 및 인접리스트, 진입차수 리스트 생성, 자기 자신을 짓는데 걸리는 시간 저장 리스트
n = int(input())                                    # 건물의 개수 n을 입력받습니다
A = [[] for _ in range(n+1)]                        # 그래프의 연결관계를 저장할 인접 리스트 A를 생성합니다
indegree = [0] * (n+1)                              # 각 건물의 진입차수를 저장할 리스트 생성
selfBuild = [0] * (n+1)                             # 각 건물이 자신을 짓는데 걸리는 시간을 저장할 리스트 생성(가중치 저장 리스트)

# 2. 그래프 생성(각 건물의 건설 시간 및 선행 건물 정보 입력)
for i in range(1, n+1):                             # 1번 n번 건물까지 반복
    inputlist = list(map(int, input().split()))     # '건설시간'과 '선행 건물 목록'을 한 줄씩 입력받아 리스트 저장
    selfBuild[i] = (inputlist[0])                   # 입력 받은 리스트의 첫번째 값을 i번 건물의 건설 시간으로 저장
    index = 1                                       # 선행 건물 목록을 탐색하기 위한 인덱스를 1로 초기화
    while True:                                     # 선행 건물이 끝날 때까지 반복
        preTemp = inputlist[index]                  # 현재 인덱스의 값을 임시 변수에 저장
        index += 1                                  # 다음값을 보기 위해 인덱스를 증가
        if preTemp == -1:                           # 만약 입력 값이 -1이면
            break                                   # 반복문 종료
        A[preTemp].append(i)                        # '선행 건물'이 끝나야 '현재 건물(i)'를 지을 수 있으므로, preTemp → i 방향의 간선을 지정합니다
        indegree[i] += 1                            # 현재 건물 i 의 진입 차수를 1 증가시킵니다

# 3. 위상 정렬 수행
que = deque()                                       # 큐 생성

for i in range(1, n+1):                             # 1번 건물부터 n번 건물까지 반복
    if indegree[i] == 0:                            # 현재 건물 i의 진입 차수가 0이면
        que.append(i)                               # 큐에 해당 건물 번호를 추가합니다

res = [0] * (n+1)                                   # 결과값(선행 건물들까지 모두 짓는데 걸리는 시간)을 저장할 리스트 생성 및 초기화

while que:                                          # 큐가 빌때까지
    now = que.popleft()                             # 큐에서 현재 처리할 건물을 꺼냅니다
    for next in A[now]:                             # 현재 건물 now가 끝난 후 지을 수 있는 다음 건물(next)를 순회합니다
        indegree[next] -= 1                         # 다음 건물 next의 진입 차수를 1 감소시킵니다

        # 핵심 로직: 다음 건물 next의 최소 시작 가능 시간을 갱신
        # 다음 건물의 시작 가능 시간(res[next])은 '기존에 계산된 선행 완료 시간'과 '현재 건물 now의 완료 시간(res[now] + selfBuild[now])' 중
        # 더 큰 값으로 갱신해야 합니다(모든 선행 건물이 완료되어야 시작 가능)
        res[next] = max(res[next], res[now] + selfBuild[now])
        if indegree[next] == 0:                     # 다음 건물 next의 진입 차수가 0이 되었다면
            que.append(next)                        # 큐에 next 건물을 추가합니다

# 4. 위상 정렬 결과 출력
for i in range(1, n+1):                             # 1번 건물부터 n번 건물까지 반복하여
    print(res[i] + selfBuild[i])                    # 최종 결과를 출력