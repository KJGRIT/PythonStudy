import sys
input = sys.stdin.readline

h = int(input())
m = int(input())
l = int(input())
coke = int(input())
sprite = int(input())

burger = [h,m,l]
drink = [coke, sprite]

print(min(burger)+min(drink)-50)
