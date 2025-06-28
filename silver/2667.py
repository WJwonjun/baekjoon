from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N = int(input())
maps = [list(map(int, input().strip())) for _ in range(N)]
count = 0
sizes = []
visited = [[False] * N for _ in range(N)]
for i in range(N):
  for j in range(N):

    if maps[i][j] == 1 and visited[i][j] == False:
      Q = deque([(i, j)])
      count += 1
      size = 1
      visited[i][j] = True

      while Q:
        y, x = Q.popleft()
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
          ny, nx = y + dy, x + dx
          if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] == 1 and visited[ny][nx] == False:
              visited[ny][nx] = True
              size += 1
              Q.append((ny, nx))
      sizes.append(size)
print(count)
sizes.sort()
for size in sizes:
  print(size)
