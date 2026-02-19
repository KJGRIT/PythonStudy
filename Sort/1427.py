import sys
input = sys.stdin.readline

a = list(map(str,input().rstrip()))
a.sort(reverse=True)
for i in a:
    print(i, end='')