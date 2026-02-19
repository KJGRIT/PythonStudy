import sys
input = sys.stdin.readline

n = int(input())
# 1.첫번째 방법
# cnt2, cnt5 = 0, 0

# for i in range(1, n+1):
#     x = i
    
#     while x % 2 == 0:
#         x //= 2
#         cnt2 += 1
#     while x % 5 == 0:
#         x //= 5
#         cnt5 += 1
    
# print(min(cnt2,cnt5))

# 2. 두번째 방법
# cnt5 = 0

# for i in range(1, n+1):
#     x = i 
    
#     while x % 5 == 0:
#         x //= 5
#         cnt5 += 1
        
# print(cnt5)

#3. 세번째 방법
res = n//5 + n//(5**2) + n//(5**3)
print(res)