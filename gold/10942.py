import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp  = [[False]*(N) for _ in range(N)]

for i in range(N):
    dp[i][i]=True

for i in range(N-1):
    dp[i][i+1] = (nums[i]==nums[i+1])

for length in range(3,N+1):
    for start in range(N-length+1):
        end = start+length-1
        if nums[start]==nums[end] and dp[start+1][end-1]:
            dp[start][end]=True



for i in range(M):
    S,E = map(int,input().split())
    print(1 if dp[S-1][E-1]==True else 0)