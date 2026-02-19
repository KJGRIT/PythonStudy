import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a,b = map(int, input().split())
#    g = math.gcd(a,b)
    
#    print(a*b//g)
    
    l = math.lcm(a,b)
    print(l)
    
# def gcd(a,b):
#     while b != 0:
#         a,b = b,a%b
#     return a
    
# for _ in range(T):
#     a,b = map(int, input().split())
#     print(a*b//gcd(a,b)) 