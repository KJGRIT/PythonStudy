import sys
input = sys.stdin.readline

a,b = map(int,input().split())
c = list(map(int, input().split()))
pre_sum = [0]
temp = 0 
for i in c:
    temp += i 
    pre_sum.append(temp)
#print(pre_sum)

for i in range(b):
    s,e = map(int, input().split())
    d=pre_sum[e]-pre_sum[s-1]
    print(d)
