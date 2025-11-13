import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
M = int(input())

dp = [[-1]*(N) for _ in range(M+1)]

def make_num(a,b):
    if a==-1 :return b

    if a==0:
        return b*10
    
    if b==0:
        return a*10
    
    return max(int(str(a)+str(b)), int(str(b)+str(a)))

for i in range(M+1):  # 가격
    for j in range(N): # 숫자
        tmp = i
        if tmp-P[j]>=0: #구매가 가능한 경우
            dp[i][j] = max(max(dp[i-1]),make_num(max(dp[tmp-P[j]]),j)) # 안사기, j를 무조건 사기
        else:
            dp[i][j] = max(dp[i-1])

    #print(i, dp[i])
print(max(dp[-1]))