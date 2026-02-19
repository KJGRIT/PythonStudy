import sys
input = sys.stdin.readline

a,b,c,n = map(int,input().split())
ans = 0

# A =[c,b,a]
#
# for i in A:
#     if n % i == 0:
#         print(1)
#         break
#     else:
#         n = n % i
#
# if n % a != 0:
#     print(0)
#

for x in range(n // a+1):
    for y in range(n // b+1):
        for z in range(n // c+1):
            if a*x + b*y + c*z == n:
                ans = 1
                break
            if ans == 1:
                break
        if ans == 1:
            break

print(ans)

