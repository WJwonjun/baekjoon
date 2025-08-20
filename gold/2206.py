import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
map = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
start = ((0, 0),1, 0)

queue = deque([start])
visited = [[[False] * M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = True



while queue:
    (y, x), time, bomb = queue.popleft()
    if y == N - 1 and x == M - 1:
        print(time)
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1 and not bomb :
                visited[1][ny][nx] = True
                queue.append(((ny, nx), time + 1, 1))
            elif map[ny][nx] == 0 and not visited[bomb][ny][nx]:
                visited[bomb][ny][nx] = True
                queue.append(((ny, nx), time + 1, bomb))
                
else:
    print(-1)