from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

input = sys.stdin.read().split()
N = int(input[0])
M = int(input[1])
S = input[2]

count = 0
i = 0
pattern = 0

while i < M - 1:
  if S[i:i + 3] == 'IOI':
    pattern += 1
    i += 2
    if pattern >= N:
      count += 1
  else:
    pattern = 0
    i += 1
print(count)
