import sys
input = sys.stdin.readline

number = []
res = 0

for i in range(5):
    student = int(input())
    number.append(student)
    
    if number[i] < 40:
        number[i] = 40
    
    res = sum(number)//5
    
print(res)
    
                