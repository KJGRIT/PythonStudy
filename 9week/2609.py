import sys
import math
input = sys.stdin.readline

a,b = map(int, input().split())
g = math.gcd(a,b)
l = math.lcm(a,b)

print(g)
# print(a *b//g)
print(l)