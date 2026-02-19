import sys
input = sys.stdin.readline

N = int(input())
W = []

for i in range(N):
    x,y = map(int,input().split())
    W.append((x,y))

ans = []

for i in range(N):
    k = 0
    for j in range(N):
        if W[i][0] < W[j][0] and W[i][1] < W[j][1]:
            k += 1
    ans.append(k + 1)

print(*ans)




