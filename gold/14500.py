from os import times_result
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
maximum = 0

def dfs(x,y,tmp,cnt):
    global maximum
    if cnt==4:
        maximum = max(maximum,tmp)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<M and 0<=ny<N and visited[ny][nx]==False:
            visited[ny][nx] = True
            dfs(nx,ny,tmp+maps[ny][nx],cnt+1)
            visited[ny][nx] = False 
    

def fy(x, y):
    global maximum
    tmp = maps[y][x]
    arr = []
    for i in range(4): # 모든 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N:
            arr.append(maps[ny][nx])
    length = len(arr)
    if length == 4 : 
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) +tmp)
    elif length == 3: 
        maximum = max(maximum, sum(arr) + tmp)
    return 

for i in range(N):
    for j in range(M):
        visited[i][j] = True 
        dfs(j, i, maps[i][j], 1)
        fy(j, i)
        visited[i][j] = False

print(maximum)