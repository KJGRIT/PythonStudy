import sys
input = sys.stdin.readline

# x,y,z = map(int, input().split())

# if x == y == z:
#     print(10000+x*1000)
# elif x == y:
#     print(1000+x*100)
# elif x == z:
#     print(1000+x*100)
# elif y == z:
#     print(1000+y*100)
# else:
#     print(max(x,y,z)*100)

a = list(map(int, input().split()))
a.sort()
if a[0] == a[2]:
    print(10000+a[0]*1000)
elif a[0] == a[1] or a[1] == a[2]:
    print(1000+a[1]*100)
else:
    print(max(a)*100)