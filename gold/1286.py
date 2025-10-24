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

# 각 글자 기준으로, 상하좌우 격자를 고른다고 생각하자. 
# 상-> i 위에서 자유롭게 선택하므로 i+1, 하 -> i 밑에서 선택하므로 2*N-i, 좌->j 왼쪽에서 선택하므로 j+1, 우-> j 오른쪽에서 선택하므로 (2*M-j)
# 이를 확장된 사각형을 고려하여 계산한다. 
for v in ans:
    print(v)
