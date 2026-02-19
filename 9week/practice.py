import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

p = [1] * (m+1)
p[1] = 0 
y = int(m ** 0.5)

for i in range(2, y+1):
    if p[i] == 1:
        for j in range(i+i, m+1, i):
            p[j] = 0
            
res = []

for i in range(n, m+1):
    if p[i] == 1:
        res.append(i)
        
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(res[0])