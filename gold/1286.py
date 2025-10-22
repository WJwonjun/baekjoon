import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]
ans = [0] * 26

for i in range(N):
    for j in range(M):
        c = ord(maps[i][j]) - 65
        total = (
            (i+1)*(j+1)*(2*N - i)*(2*M - j)
          + (i+1)*(M + j + 1)*(2*N - i)*(M - j)
          + (N + i + 1)*(j + 1)*(N - i)*(2*M - j)
          + (N + i + 1)*(M + j + 1)*(N - i)*(M - j)
        )
        ans[c] += total

for v in ans:
    print(v)
