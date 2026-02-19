import sys
input = sys.stdin.readline

output = []

while True:
    a,b,c = map(int, input().split())
    x,y,z = sorted([a,b,c])
    
    if z*z == x*x + y*y and a != 0 and b != 0 and c != 0:
        output.append("right")
    elif a == 0 and b == 0 and c == 0:
        break
    else:
        output.append("wrong")
        
print("\n".join(output))
        