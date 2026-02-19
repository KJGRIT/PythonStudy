import sys
input = sys.stdin.readline

N,m,M,T,R = map(int, input().split())
res = 0
cnt = 0
now = m

if m + T > M:
    print(-1)
else:
    while True:
        if now + T <= M:
            now += T
            cnt += 1
        else:
            now -= R
            now = max(now, m) # 변수 대비
    
        res += 1
        
        if N == cnt:
            break
    
    print(res)        