import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(N)]

prefix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = nums[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]



for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())  # (row1, col1, row2, col2)
    result = (
        prefix[y2][x2]
        - prefix[y1-1][x2]
        - prefix[y2][x1-1]
        + prefix[y1-1][x1-1]
    )
    print(result)