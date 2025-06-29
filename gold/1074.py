from os import times_result
import sys
from collections import deque
# Replit에서는 input.txt를 stdin으로 사용하게 설정
if sys.stdin.isatty():
    sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N, r, c = map(int, input().split())


def z(n, x, y):
    if n == 0:
        return 0
    half = 2**(n - 1)
    if r < x + half and c < y + half:
        return z(n - 1, x, y)
    elif r < x + half and c >= y + half:
        return half * half + z(n - 1, x, y + half)
    elif r >= x + half and c < y + half:
        return 2 * half * half + z(n - 1, x + half, y)
    else:
        return 3 * half * half + z(n - 1, x + half, y + half)


print(z(N, 0, 0))
