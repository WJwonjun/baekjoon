from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
M, N, H = map(int, input().split())
tomatos = [[list(map(int,
                     input().split())) for i in range(N)] for j in range(H)]


def bfs(M, N, H):
  flag = 0
  for i in range(H):
    if flag == 1:
      break
    for j in range(N):
      if flag == 1:
        break
      for k in range(M):
        if tomatos[i][j][k] != 1:
          flag = 1
          break
  if flag == 0:
    return 0
  Q = deque()
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if tomatos[i][j][k] == 1:
          Q.append((i, j, k))
  count = 0
  while Q:
    for _ in range(len(Q)):
      z, y, x = Q.popleft()
      for dz, dy, dx in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0),
                         (1, 0, 0), (-1, 0, 0)]:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomatos[nz][ny][
            nx] == 0:
          tomatos[nz][ny][nx] = 1
          Q.append((nz, ny, nx))
    count += 1

  for i in range(H):
    for j in range(N):
      for k in range(M):
        if tomatos[i][j][k] == 0:
          return -1
  return count - 1


print(bfs(M, N, H))
