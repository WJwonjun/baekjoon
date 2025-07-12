import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
dp = [-1]*1000001
dp[N]=0

Q = deque([N])
while Q:
    current = Q.popleft()
    if current==K:
        print(dp[current])
        break

    if 0<=2*current<100001 and dp[2*current]==-1:
        dp[2*current] = dp[current]
        Q.appendleft(2*current)
    
    for next_pos in [current-1,current+1]:
        if 0<=next_pos<100001 and dp[next_pos]==-1:
            dp[next_pos]=dp[current]+1
            Q.append(next_pos)

