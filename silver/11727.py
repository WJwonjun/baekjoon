N = int(input())
dp = [0]*(N+1)
for i in range(1,N+1):
    if i==1:
        dp[i]=1
    elif i==2:
        dp[2]=3
    else:
        dp[i]=(dp[i-1]+2*dp[i-2])%10007

print(dp[N])

