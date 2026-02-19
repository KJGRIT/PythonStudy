import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())
    
stack = []
now = 1
result = True
answer = []
    
for i in range(n):
    su = a[i]
    if su >= now:
        while su >= now:
            stack.append(now)
            now += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer.append('-')
            
if result:
    for i in answer:
        print(i)