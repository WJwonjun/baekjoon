import sys
N = list(map(int,input().split()))
N.pop()

INF = float('inf')
dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(len(N)+1)]
dp[0][0][0] = 0

def cost(a,b):  #foot, target
    if a==b: return 1
    if a==0: return 2
    if abs(a-b)==2: return 4
    return 3

for i in range(1,len(N)+1):
    target = N[i-1]
    for l in range(5):
        for r in range(5):
            if dp[i-1][l][r]!=INF:
                dp[i][target][r] = min(dp[i][target][r],dp[i-1][l][r]+cost(l,target))
                dp[i][l][target] = min(dp[i][l][target],dp[i-1][l][r]+cost(r,target))


print(min([min(cols) for cols in dp[len(N)]]))


# 이거 일단 dp를 5*5*N로 만들어야 함. 단순히 왼발/오른발 옮기면 안됨 -> 이전 경우 큰거 선택 + 조금 옮기기가 더 쌀수도 있음
