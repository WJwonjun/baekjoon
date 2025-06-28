from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
G = {i: [] for i in range(N)}
for i in range(N):
  datas = list(map(int, sys.stdin.readline().split()))
  for j in range(N):
    if datas[j] == 1:
      G[i].append(j)

ways = [[0] * N for i in range(N)]

for start in range(N):
  visited = [False] * N
  Q = deque([start])
  visited[start] = True

  while Q:
    cur = Q.popleft()
    for neighbor in G[cur]:
      if not visited[neighbor]:
        visited[neighbor] = True
        ways[start][neighbor] = 1
        Q.append(neighbor)

      if neighbor == start:
        ways[start][start] = 1
for row in ways:
  print(*row)
