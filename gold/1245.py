import sys
sys.setrecursionlimit(100000)
from collections import deque



input = sys.stdin.readline
N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

d = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

cnt = 0

visited = [[False]*M for _ in range(N)]


while True:
    flag=0
    max_value = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]==False:flag=1
            if not visited[i][j] and matrix[i][j]>max_value:
                max_i,max_j = i,j
                max_value = matrix[i][j]
    visited[max_i][max_j]=True
    stack = [(max_i,max_j)]
    if flag==0:
        break

    #print(stack)
    while stack:
        y,x = stack.pop()
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and matrix[ny][nx] <= matrix[y][x]:
                        visited[ny][nx] = True
                        stack.append((ny, nx))
                        #print(ny,nx)
                        
    cnt += 1
    
    #for row in visited:
        #print(row,end='\n')
print(cnt)