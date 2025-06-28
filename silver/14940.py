from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
for i in range(N):
  row = list(map(int, input().strip().split()))
  for j in range(M):
    if row[j] == 2:
      y, x = i, j
      row[j] = 1
  maps.append(row)

Q = deque([(y, x)])
visited = [[-1] * M for _ in range(N)]
visited[y][x] = 0

while Q:
  y, x = Q.popleft()

  for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
    ny, nx = y + dy, x + dx
    if 0 <= ny < N and 0 <= nx < M:
      if maps[ny][nx] == 1 and visited[ny][nx] == -1:
        visited[ny][nx] = visited[y][x] + 1
        Q.append((ny, nx))

for i in range(N):
  for j in range(M):
    if maps[i][j] == 0:
      print(0, end=' ')
    else:
      print(visited[i][j], end=' ')
  print()
