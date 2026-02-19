import sys
import collections
input = sys.stdin.readline

n = int(input())
d = collections.defaultdict(int)

for i in range(n):
    title = input().rstrip()
    d[title] += 1

m = max(d.values())
k = list(d.keys())
k.sort()

for i in k:
    if d[i] == m:
        print(i)
        break
