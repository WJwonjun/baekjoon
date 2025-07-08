import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*3 for _ in range(N)]
    dp[0][0] = nums[0][0]
    dp[0][1] = nums[1][0]
    dp[0][2] = 0

    for i in range(1, N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + nums[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + nums[1][i]
        dp[i][2] = max(dp[i-1])
    print(max(dp[N-1]))
