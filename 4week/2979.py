import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
# t = [0]*101
# res = 0

# for i in range(3):
#     s,e = map(int, input().split())
    
#     for j in range(s,e):
#         t[j] += 1

# for i in range(1, 100):
#     if t[i] == 1:
#         res += a
#     elif t[i] == 2:
#         res += b * 2
#     elif t[i] == 3:
#         res += c * 3

t = [0]*101
p = [0, a, b*2, c*3]
res = 0

for i in range(3):
    s,e = map(int, input().split())
    
    for j in range(s,e):
        t[j] += 1

for i in range(1, 100):
    res += p[t[i]]

print(res)

    