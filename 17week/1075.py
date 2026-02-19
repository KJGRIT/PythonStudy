import sys
input = sys.stdin.readline

# n = int(input())
# f = int(input())
#
# n //= 100
# n *= 100
# res = 0
#
# for i in range(100):
#     if (n+i) % f == 0:
#         res = i
#         break
#
# if res < 10:
#     print(f'{res:02d}')
# else:
#     print(res)

n = int(input())
f = int(input())

# 1. 뒷 2자리를 00으로 만드는 과정
n //= 100
n *= 100
res = 0

# 2. n+0 ~ n+99 까지 돌면서 f로 나눠지는 처음(최소) n+i 찾기
for i in range(100):
    if (n+i) % f == 0:
        res = i
        break

# 3. 두 자리 숫자로 출력
print(f'{res:02d}')