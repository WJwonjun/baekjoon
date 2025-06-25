
N =int(input())
nums = []


for _ in range(N):
    nums.append(int(input()))
max_num = max(nums)
dp=[0]*(max_num+1)
for i in range(1,max_num+1):
    if i<=3:
        dp[i]=1
    else:
        dp[i] = dp[i-2]+dp[i-3]
for num in nums:
    print(dp[num])
