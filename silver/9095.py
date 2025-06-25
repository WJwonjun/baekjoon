N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
max_num=max(nums)
dp=[0]*(max_num+1)

for j in range(1,max_num+1):
    if j==1:
        dp[j]=1
    elif j==2:
        dp[j]=2
    elif j==3:
        dp[j]=4
    else:
        dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
        
for num in nums:
    
    print(dp[num])