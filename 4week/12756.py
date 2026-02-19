import sys
input = sys.stdin.readline

Att1, Hp1 = map(int, input().split())
Att2, Hp2 = map(int, input().split())

while True:
    Hp2 -= Att1
    Hp1 -= Att2

    if Hp1 <= 0 and Hp2 <= 0:
        print("DRAW")
        break
    elif Hp2 <= 0:
        print("PLAYER A")
        break
    elif Hp1 <= 0:
        print("PLAYER B")
        break

        
    
        