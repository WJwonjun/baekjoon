import sys
data=sys.stdin.read().split()
N, M = int(data[0]),int(data[1])
nums = list(map(int,data[2:N+2]))
pair_list = list(map(int,data[N+2:]))
pairs = list(zip(pair_list[::2],pair_list[1::2]))

dp = [0]*(N+1)
for i in range(1,N+1):
    dp[i] = dp[i-1]+nums[i-1]
for j,k in pairs:
    result = 0
    print(dp[k]-dp[j-1])
