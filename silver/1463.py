N = int(input())
dp = [0]*(N+1)



for i in range(1,N+1):
    d2 = i%2
    d3 = i%3
    if i==1:
        dp[i]=0
    elif d3==0:
        if d2==0:
            dp[i]=min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
        else:
            dp[i]=min(dp[i//3]+1,dp[i-1]+1)
    elif d3==1:
        if d2==0:
            dp[i]=min(dp[i//2]+1,dp[i-1]+1)
        else:
            dp[i]=dp[i-1]+1
    else:
        if d2==0:
            dp[i]=min(dp[i//2]+1,dp[i-1]+1)
        else:
            dp[i]=dp[i-1]+1
print(dp[N])