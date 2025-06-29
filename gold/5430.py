from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
  sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
T = int(input())
for _ in range(T):
  cmds = list(input().strip())
  length = int(input())
  nums = input().strip()
  flag = 1
  Q = deque(nums[1:-1].split(',')) if length != 0 else deque()
  R = 0
  for cmd in cmds:
    if cmd == 'R':
      R += 1
    elif cmd == 'D':
      if len(Q) == 0:
        print('error')
        flag = 0
        break
      else:
        if R % 2 == 0:
          Q.popleft()
        else:
          Q.pop()
  if flag == 0:
    continue
  else:
    if R % 2 == 0:
      print('[' + ','.join(Q) + ']')
    else:
      Q.reverse()
      print('[' + ','.join(Q) + ']')
