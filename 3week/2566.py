import sys
input = sys.stdin.readline

# a=[]


# for i in range(9):
#     b = list(map(int, input().split()))
#     a.append(b)
    
# res = a[0][0]
# idx = [1,1]
# for x in range(9):
#     for j in range(9):
#         if res < a[x][j]:
#             res = a[x][j]   
#             idx = [x+1, j+1]     

val = -1
idx = [1,1]

for i in range(9):
    a = list(map(int,input().split()))
    # print(a)
    for j in range(9):
        if val < a[j]:
            val = a[j]
            idx = [i+1, j+1]

print(val)
print(*idx)
