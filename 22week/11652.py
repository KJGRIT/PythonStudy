import sys
import collections
input = sys.stdin.readline

n = int(input())
d = collections.defaultdict(int)

for i in range(n):
    x = int(input())
    d[x] += 1

m = max(d.values())
k = list(d.keys())
k.sort()

for x in k:
    if d[x] == m:
        print(x)
        break