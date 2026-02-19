import sys
input = sys.stdin.readline

# n = input()
# numbers = list(map(int,input()))
# sum = 0

# for i in numbers:
#     sum += i 

n = input()
numbers = input().rstrip()
sum = 0

for i in numbers:
    sum += int(i)
print(sum)