import sys
from collections import deque
input=  sys.stdin.readline
M,N = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

def bfs():
    flag = 0
    for i in range(N):
        if flag==1:
            break
        for j in range(M):
            if maps[i][j]==0:
                flag=1
                break
    if flag==0:
        return 0
    
    Q = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j]==1:
                Q.append((i,j))
    count = 0
    while Q:
        for _ in range(len(Q)):
            y,x = Q.popleft()
            for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny,nx =  y+dy,x+dx
                if 0<=ny<N and 0<=nx<M and maps[ny][nx]==0:
                    maps[ny][nx]=1
                    Q.append((ny,nx))
        count+=1
    for i in range(N):
        for j in range(M):
            if maps[i][j]==0:
                return -1
    return count-1

print(bfs())
