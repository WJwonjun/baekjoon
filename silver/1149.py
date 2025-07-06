import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
homes = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    homes[i][0] = min(homes[i-1][1],homes[i-1][2]) + homes[i][0]
    homes[i][1] = min(homes[i-1][0],homes[i-1][2]) + homes[i][1]
    homes[i][2] = min(homes[i-1][0],homes[i-1][1]) + homes[i][2]

print(min(homes[N-1][0],homes[N-1][1],homes[N-1][2]))