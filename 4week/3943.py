import sys
input = sys.stdin.readline

T = int(input())

# for i in range(T):
#     N = int(input())
#     res = N
    
#     while N > 1:
#         if N%2 == 0:
#             N//=2
#         else:
#             N = 3*N + 1
#         res = max(res, N)

for i in range(T):
    n = int(input())
    res = n
    
    while n > 1:
        if n % 2 == 0:
            n //=2
        else:
            n = 3*n + 1
            res = max(res, n)
    print(res)