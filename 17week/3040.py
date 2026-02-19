import sys
input = sys.stdin.readline

# a = []
#
# for i in range(9):
#     x = int(input())
#     a.append(x)
#
# for i1 in range(9):
#     for i2 in range(i1+1, 9):
#         for i3 in range(i2+1, 9):
#             for i4 in range(i3+1, 9):
#                 for i5 in range(i4+1, 9):
#                     for i6 in range(i5+1, 9):
#                         for i7 in range(i6+1, 9):
#                             if a[i1]+a[i2]+a[i3]+a[i4]+a[i5]+a[i6]+a[i7] == 100:
#                                 print(a[i1])
#                                 print(a[i2])
#                                 print(a[i3])
#                                 print(a[i4])
#                                 print(a[i5])
#                                 print(a[i6])
#                                 print(a[i7])

a = []
s = 0
res = []

for i in range(9):
    x = int(input())
    a.append(x)
    s += x

for i in range(9):
    for j in range(i+1, 9):
        if s - a[i] - a[j] == 100:
            res = [i, j]

for i in range(9):
    if i not in res:
        print(a[i])