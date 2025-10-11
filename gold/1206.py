import sys
input = sys.stdin.readline

N = int(input())
#print(301*106, 302*106)

nums_prime = []
for _ in range(N):
    A_str = input()
    if '.' in A_str:
        parts = A_str.split('.')
        # 소수점 아래 3자리까지 맞추기 위해 rjust 사용
        decimal_part = parts[1].ljust(3, '0')
        A_int = int(parts[0] + decimal_part)
    else:
        A_int = int(A_str) * 1000
    nums_prime.append(A_int)
#print(nums)
# input 자체를 string으로 받는 방법 필요 
# 왜냐 ->  float 3.1 -> 컴퓨터에서는 3.09999999999로 인식
cnt = 1
while True:
    for num in nums_prime: #O(N)
        a = num*cnt
        b = (num+1)*cnt
        c = ((a +1000) // 1000) * 1000
        if a%1000==0:
            c-=1000
        #print(cnt,a,b,c)
        if b<=c:
            cnt+=1
            break
    else:
        print(cnt)
        break
    