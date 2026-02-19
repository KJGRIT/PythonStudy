import sys
input = sys.stdin.readline

n,x,k = map(int, input().split())
# chk = [0]*(n+1)
# chk[x] = 1

# for i in range(k):
#     a,b = map(int, input().split())
#     chk[a], chk[b] = chk[b], chk[a]

# for i in range(1, n+1):
#     if chk[i] == 1:
#         print(i)
#         break

#디버깅해도 이해가 안감
for i in range(k):
    a,b = map(int, input().split())
    
    if x == a:
        x = b
    elif x == b:
        x = a
print(x)