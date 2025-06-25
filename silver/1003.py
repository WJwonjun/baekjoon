import sys
data = sys.stdin.read()
T = int(data[0])
nums = list(map(int,data[1:].split()))
max_num = max(nums)

dp = [[0, 0] for _ in range(max_num + 1)]
dp[0] = [0,1]
if max_num>=1:
    dp[1] = [1,0]
    
for i in range(2, max_num + 1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for num in nums:
    print(dp[num][0], dp[num][1])
