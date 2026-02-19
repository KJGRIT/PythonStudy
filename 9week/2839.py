import sys
input = sys.stdin.readline
#1. n 입력 받기
n = int(input())
res = -1

for i in range(5):
    m = n - 3 * i
    if m == 0 or m % 5 == 0:
        res = m // 5 + i
    elif m < 0:
        break

print(res)

