import sys
input = sys.stdin.readline

#1. 입력 받기
n = int(input())
a = list(map(int, input().split()))
res = 0

#2. 원소마다 검사
for x in a:
    if x == 1:                      # 원소가 1이면 건너띄기
        continue
    flag = 0                        # 소수 확인 변수
    
    y = int(x ** 0.5)               # x의 제곱근 정수 부분만(목적: 반복을 줄이기 위해서)
    
    for i in range(2, y+1):         # x가 소수인지 확인하기 위해 x의 약소가 있는지 검사
        if x % i == 0:              # x가 약수이면
            flag = 1                # flag = 1로 변환
            break                   # 반복문 탈출
    
    if flag == 0:                    # 소수이면
        res += 1                    # 카운트 

#3. 카운트 결과값 출력       
print(res)
    
    