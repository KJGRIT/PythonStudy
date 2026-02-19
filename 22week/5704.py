import sys
input = sys.stdin.readline

# while True:
#     a = input().rstrip()
#
#     if a == '*':
#         break
#
#     b = [0] * 26
#
#     for x in a:
#         if x.islower():
#             b[ord(x)-ord('a')] = 1
#
#     if sum(b) == 26:
#         print('Y')
#     else:
#         print('N')

while True:
    a = input().rstrip()

    if a == '*':
        break

    s = set()

    for x in a:
        if x.islower():
            s.add(x)

    if len(s) == 26:
        print('Y')
    else:
        print('N')

