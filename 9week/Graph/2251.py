import sys
from collections import deque
input = sys.stdin.readline

Sender = [0,0,1,1,2,2]                                                  # 물을 보내는 물통 인덱스
Receiver = [1,2,0,2,0,1]                                                # 물을 받는 물통 인덱스
now = list(map(int, input().split()))                                   # A,B,C 물통의 용량
visited = [[False for j in range(201)] for i in range(201)]             # visited[a][b] 가 True 이면 (a,b,c)의 상태를 방문한 적이 있음
answer = [False] * 201                                                  # A가 0일 때 C의 가능한 물의 양을 기록하는 배열

def BFS():                                                              #
    que = deque()                                                       # BFS를 위한 큐 생성
    que.append((0,0))                                                   # 초기 상태 : A=0, B=0,C=now[2]
    visited[0][0] = True                                                # 시작 상태 방문 체크
    answer[now[2]] = True                                               # 처음 상태에서의 c의 물량 기록
    while que:                                                          # 큐가 빌 때까지 반복
        now_node = que.popleft()                                        # 현재 상태 꺼내기
        A = now_node[0]
        B = now_node[1]
        C = now[2] - A - B                                              # c는 전체 물 now[2]에서 a + b를 뺀 값
        for k in range(6):                                              # 6가지 물 붓기 경우에 대해 탐색
            next = [A,B,C]                                              # 다음 상태 준비
            next[Receiver[k]]+=next[Sender[k]]                          # 물을 붓기(받는 물통에 추가)
            next[Sender[k]] = 0                                         # 보내는 물통 = 0
            if next[Receiver[k]] > now[Receiver[k]]:                    # 받는 물통이 넘칠 경우 처리(초과분을 다시 sender로 되돌림)
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]]
                next[Receiver[k]] = now[Receiver[k]]
            if not visited[next[0]][next[1]]:                           # (a,b)를 기준으로 방문 여부 체크
                visited[next[0]][next[1]] = True
                que.append(next[0],next[1])                             # 다음 상태 큐에 삽입
                if next[0] == 0:                                        # A가 0이면 C 용량 결과에 기록
                    answer[next[2]] = True

BFS()

for i in range(len(answer)):                                            # 가능한 C의 물의 양만 출력
    if answer[i]:
        print(i, end=' ')