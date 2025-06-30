import sys
from collections import deque
input=  sys.stdin.readline

N = int(input())
maps = [list(input().strip()) for _ in range(N)]
maps2 = [row[:] for row in maps]

count=0
for i in range(N):
    for j in range(N):
        if maps[i][j]!='O':
            Q = deque([(i,j)])
            key = maps[i][j]
            while Q:
                y,x = Q.popleft()
                for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ny,nx = y+dy, x+dx
                    if 0<=ny<N and 0<=nx<N and maps[ny][nx]==key:
                        maps[ny][nx] = 'O'
                        Q.append((ny,nx))
            count+=1


for i in range(N):
    for j in range(N):
        if maps2[i][j]=='G':
            maps2[i][j]='R'
count2 = 0


for i in range(N):
    for j in range(N):
        if maps2[i][j]!='O':
            Q = deque([(i,j)])
            key = maps2[i][j]
            while Q:
                y,x = Q.popleft()
                for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ny,nx = y+dy, x+dx
                    if 0<=ny<N and 0<=nx<N and maps2[ny][nx]==key:
                        maps2[ny][nx] = 'O'
                        Q.append((ny,nx))
            count2+=1
print(count,count2)
