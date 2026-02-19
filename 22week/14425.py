import sys
input = sys.stdin.readline

n,m = map(int,input().split())
M = []
s = set()
cnt = 0

for i in range(n):
    s.add(input().rstrip())

for i in range(m):
    M.append(input().rstrip())
    if M[i] in s:
        cnt += 1

print(cnt)