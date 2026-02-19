import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

p = [1] * 1001
p[1] = 0
y = int(1000 ** 0.5)

# for i in range(2, y+1):
#     if p[i] == 1:
#         for j in range(i*2, 1001, i):
#             p[j] = 0
            
# res = 0

# for x in a:
#     if p[x] == 1:
#         res += 1

for i in range(2, y + 1):
    if p[i] == 1:
        for j in range(i + i, 1001, i):
            p[j] = 0

res = 0

for x in a:
    res += p[x]        

print(res)