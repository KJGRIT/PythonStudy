import sys
input = sys.stdin.readline

s = set()

for i in range(10):
    x = int(input())
    s.add(x%42)

print(len(s))