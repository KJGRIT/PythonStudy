import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = max(a)

# for i in range(n):
#     a[i] = a[i] / m * 100

# res = sum(a)/n
# print(res)

res = sum(a) / n
res = res / m * 100 

print(res)   