import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    age, name = input().split()
    a.append((int(age),i,name))

a.sort()

for age, i, name in a:
    print(age,name)
