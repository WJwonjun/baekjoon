import sys
input = sys.stdin.readline
N = int(input())
INF = int(1e9)

maps = [ list(map(int,input().split(' '))) for _ in range(N)]

dp = [[int(1e9)]*N for _ in range(3)]

answer = INF

for first in range(3):
    dp = [[INF]*3 for _ in range(N)]

    dp[0][first] = maps[0][first]

    for i in range(1,N):
        for c in range(3):
            dp[i][c] = min(dp[i-1][k] for k in range(3) if k!=c) + maps[i][c]
    
    for last in range(3):
        if first==last:
            continue
        answer = min(answer, dp[N-1][last])
print(answer)