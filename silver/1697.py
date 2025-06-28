import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
visited = [0] * (100001)

Q = deque([N])
while Q:
  current = Q.popleft()
  if current == K:
    print(visited[current])
    break
  for step in (current - 1, current + 1, current * 2):
    if 0 <= step <= 100000 and not visited[step]:
      visited[step] = visited[current] + 1
      Q.append(step)
