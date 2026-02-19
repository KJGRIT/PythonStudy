import sys
import collections
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

d = collections.defaultdict(int)

for i in a:
    d[i] += 1

for i in b:
    print(d[i], end=' ')

