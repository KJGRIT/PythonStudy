import sys
input = sys.stdin.readline

n = int(input())
output = []

def gcd(a,b):
    while b != 0:
        return gcd(b,a%b)
    return a 
    
for _ in range(n):
    a,b = map(int, input().split())
    res = a*b // gcd(a,b)
    output.append(str(res))
    
print('\n'.join(output))