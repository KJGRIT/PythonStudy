import sys
input = sys.stdin.readline

seq = input().rstrip()
a = 1

# for i in seq:
#     if i == 'A':
#         if a == 1:
#             a = 2
#         elif a == 2:
#             a = 1
#     elif i == 'B':
#         if a == 2:
#             a = 3
#         elif a == 3:
#             a = 2
#     elif x == 'C':
#         if a == 1:
#             a = 3
#         elif a == 3:
#             a = 1 

for i in seq:
    if i == 'A' and a !=3:
        a = 3-a
    elif i == 'B' and a !=1:
        a = 5-a
    elif i == 'C' and a !=2:
        a = 4-a
print(a)

 