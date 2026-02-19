import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
res = 32

for i in range(n):
    x = input().rstrip()
    a.append(x)

for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0 and a[x][y] == 'B':
                    cnt += 1
                elif (x+y) % 2 == 1 and a[x][y] == 'W':
                    cnt += 1

        res = min(res, cnt, 64-cnt)

print(res)

