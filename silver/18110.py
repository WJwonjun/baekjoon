import sys

input = sys.stdin.readline
N = int(input())

if N == 0:
    print(0)
else:
    data = list(map(int, sys.stdin.read().split()))
    scores = data[:N]

    scores.sort()
    cut = int(N * 0.15 + 0.5)
    trimmed = scores[cut:N - cut]

    print(int(sum(trimmed) / len(trimmed) + 0.5))