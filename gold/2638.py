import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
graph[0][0] = -1
queue = deque([(0, 0)])  # (y, x)
while queue:
    y,x = queue.popleft()
    if y == N - 1 and x == M - 1:
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0 :
                graph[ny][nx] = -1
                queue.append((ny, nx))

cheezes = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cheezes.append((i, j,False))
################################################
t = 0
while True:
    now_melted = deque()
    for i in range(len(cheezes)):
        y,x, melted = cheezes[i]
        if melted:
            continue
        cnt = 0
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == -1:
                cnt += 1
            if cnt >= 2:
                cheezes[i] = (y, x, True)
                now_melted.append((y, x))
                break

    if not now_melted:
        print(t)
        break
    
    for y,x in now_melted:
        graph[y][x]=-1

    while now_melted:
        y,x = now_melted.popleft()
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny,nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                graph[ny][nx] = -1
                now_melted.append((ny, nx))

    t+=1