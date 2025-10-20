import sys,heapq

input = sys.stdin.readline

N = int(input())
mat=[]
for i in range(N):
    x,y = map(int,input().split())
    mat.append((x,y))
dp = [[0]*N for _ in range(N)]

for length in range(1,N):
    for i in range(N-length):
        j = i+length
        dp[i][j] = float('inf')
        for k in range(i,j):
            cost = dp[i][k]+dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1]
            dp[i][j] = min(dp[i][j],cost)
print(dp[0][N-1])

# 길이 먼저 돌리기 -> 안에 작은 단위들부터 채우고 키우기
# 단순 i,j,k 두면 안됨