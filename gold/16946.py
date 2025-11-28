import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
maps = []

for i in range(N):
    maps.append( list(map(int,list(input().strip()))))

kv = dict()
id=2
for i in range(N):
    for j in range(M):
        if maps[i][j]==0:

            maps[i][j] = id
            cnt=1
            Q = deque([(i,j)])
            while Q:
                y,x = Q.popleft()
                for dy,dx in ((-1,0),(1,0),(0,-1),(0,1)):
                    ny,nx = y+dy,x+dx
                    if 0<=ny<N and 0<=nx<M:
                        if maps[ny][nx]==0 :
                            Q.append((ny,nx))
                            maps[ny][nx]=id
                            cnt+=1

            kv[id] = cnt%10
            id+=1


for i in range(N):
    row = []
    for j in range(M):
        if maps[i][j] != 1:
            row.append('0')
        else:
            cnt=1
            s = set()
            for dy,dx in ((-1,0),(1,0),(0,-1),(0,1)):
                ny,nx = i+dy,j+dx
                if 0<=ny<N and 0<=nx<M: 
                    cid = maps[ny][nx]
                    if cid>=2 and cid not in s:
                        cnt+=kv[cid]
                        cnt%=10
                        s.add(cid)
            row.append(str(cnt))
    print("".join(row))