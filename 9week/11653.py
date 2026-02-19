import sys
input = sys.stdin.readline

n = int(input())
a = 2

while n > 1:
    while n % a == 0:
        print(a)
        n //= a 
    a += 1