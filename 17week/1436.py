import sys
input = sys.stdin.readline

# N = int(input())
# res = []
# k= 666
#
# for i in range(200000):
#     if '666' in str(k):
#         res.append(k)
#     k += 1
#
# print(res[N-1])

N = int(input())
k = 666
cnt = 0

while True:
    if '666' in str(k):
        cnt += 1

    if cnt == N:
        print(k)
        break

    k += 1

