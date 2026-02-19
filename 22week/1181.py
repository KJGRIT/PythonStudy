import sys
input = sys.stdin.readline

n = int(input())
s = set()

for i in range(n):
    s.add(input())

s = list(s)
s.sort(key=lambda x:(len(x),x))

print(*s, sep ='')
