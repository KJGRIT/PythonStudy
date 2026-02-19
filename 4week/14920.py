import sys
input = sys.stdin.readline

a = int(input())
cnt = 1

while a:
    if a%2 == 0:
        a//=2
    elif a == 1:
        break
    else:
        a=3*a+1
    cnt += 1
print(cnt)
    