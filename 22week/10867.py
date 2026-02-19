import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int,input().split()))

a = list(a)
a.sort()
print(*a)
