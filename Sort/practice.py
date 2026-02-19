import sys
input = sys.stdin.readline

s = input().rstrip()
a = []

for i in range(len(s)):
    a.append(s[i:])

a.sort()

for i in a:
    print(i)