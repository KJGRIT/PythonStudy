import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
temp = 0
prefix_sum = [0]

for i in range(n):
    temp += num[i]
    prefix_sum.append(temp)
    
for x in range(m):
    s,e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
    
