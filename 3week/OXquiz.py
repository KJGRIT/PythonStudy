import sys
input = sys.stdin.readline

t=int(input())
b=[]

for i in range(t):
    a=input().rstrip()
    res = 0
    v = 0
    for x in a:
        if x == 'O':
            v += 1
        else:
            v = 0
        res +=v 
    b.append(res)
print(*b)
