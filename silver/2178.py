from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

Q = deque([(0, 0)])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

while Q:
  y, x = Q.popleft()

  if y == N - 1 and x == M - 1:
    print(visited[y][x])
    break

  for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
    ny, nx = y + dy, x + dx
    if 0 <= ny < N and 0 <= nx < M:
      if maze[ny][nx] == 1 and visited[ny][nx] == 0:
        visited[ny][nx] = visited[y][x] + 1
        Q.append((ny, nx))
