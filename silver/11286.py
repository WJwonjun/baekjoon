from os import times_result
import sys
import heapq
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
heap = []
for i in range(N):
  cmd = int(sys.stdin.readline())
  if cmd != 0:
    heapq.heappush(heap, (abs(cmd), cmd))
  else:
    if not heap:
      print(0)
    else:
      print(heapq.heappop(heap)[1])
