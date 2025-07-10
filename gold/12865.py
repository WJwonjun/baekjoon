import sys
from collections import defaultdict
input = sys.stdin.readline

N,K = map(int,input().split())
things = []

for _ in range(N):
    w,v = map(int,input().split())
    things.append((w,v))

dp = [[0]*(N+1) for _ in range(K+1)]

for j in range(1,N+1): # 개수
    w,v = things[j-1]
    for i in range(1,K+1): # 무게
        if i<w:
            dp[i][j]=dp[i][j-1]
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-w][j-1]+v)
print(max(dp[-1]))