import sys
input = sys.stdin.readline

# 1. 입력 받기
n, m = map(int, input().split())
S = []
M = []
cnt = 0

# 2. 집합 S 배열과 M개의 문자열 배열 생성
for _ in range(n):
    String1 = input().rstrip()
    S.append(String1)

for _ in range(m):
    String2 = input().rstrip()
    M.append(String2)

# 3. S,M 비교 같으면 카운트
for i in S:
    for j in M:
        if i == j:
            cnt += 1
            break

# 4. 카운트 출력
print(cnt)