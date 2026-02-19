import sys
input = sys.stdin.readline

a,b,c,M = map(int, input().split())
now = 0 
cnt = 0

for i in range(24):
    if now + a <= M:
        now += a
        cnt += 1
    else:
        now -= c
        now = max(0, now)
print(cnt)