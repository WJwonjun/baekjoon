from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N = int(input())
meets = [tuple(map(int, input().split())) for _ in range(N)]
meets.sort(key=lambda x: (x[1], x[0]))

count = 1
end = meets[0][1]
for i in range(1, N):
  if meets[i][0] >= end:
    count += 1
    end = meets[i][1]
print(count)
