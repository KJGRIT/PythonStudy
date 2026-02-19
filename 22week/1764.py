import sys
input = sys.stdin.readline

n,m = map(int, input().split())
s1 = set()
s2 = set()

for i in range(n):
    s1.add(input().rstrip())

for i in range(m):
    s2.add(input().rstrip())

s = s1 & s2
s = list(s)
s.sort()

print(len(s), *s, sep='\n')
