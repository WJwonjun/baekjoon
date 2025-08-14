import sys
from collections import deque
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

toxic = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            toxic.append((i, j))

max_safe = 0
for x,y,z in combinations(range(0,N*M),3):
    if maps[x//M][x%M] == 0 and maps[y//M][y%M] == 0 and maps[z//M][z%M] == 0:
        tempmap = [row[:] for row in maps]
        tempmap[x//M][x%M] = 1
        tempmap[y//M][y%M] = 1
        tempmap[z//M][z%M] = 1

        queue = deque(toxic)
        while queue:
            cy,cx = queue.popleft()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < N and 0 <= nx < M and tempmap[ny][nx] == 0:
                    tempmap[ny][nx] = 2
                    queue.append((ny, nx))
        
        safe_count = sum(row.count(0) for row in tempmap)
        if safe_count > max_safe:
            max_safe = safe_count

print(max_safe)