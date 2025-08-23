import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

# 상어 위치/시작 처리
for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            shark_y, shark_x = i, j
            break

def bfs(sy, sx, size):
    visited = [[False]*N for _ in range(N)]
    dist    = [[-1]*N for _ in range(N)]
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    dist[sy][sx] = 0

    # 같은 거리 레벨에서 후보 모으고 (y,x) 최소 선택
    candidates = []
    min_d = None
    dirs = ((-1,0),(0,-1),(0,1),(1,0))  # 위, 왼, 오, 아래

    while q:
        y, x = q.popleft()

        # 이미 더 먼 레벨은 볼 필요 없음
        if min_d is not None and dist[y][x] > min_d:
            continue

        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 상어보다 큰 물고기면 통과 불가
                if maps[ny][nx] > size:
                    continue

                visited[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1

                if 0 < maps[ny][nx] < size:
                    if min_d is None:
                        min_d = dist[ny][nx]     # 첫 발견 거리 고정
                    if dist[ny][nx] == min_d:    # 같은 거리만 후보로
                        candidates.append((ny, nx))
                else:
                    q.append((ny, nx))

    if not candidates:
        return -1, -1, -1
    candidates.sort()             # (y,x) 우선순위
    ey, ex = candidates[0]
    return ey, ex, min_d

t = 0
size = 2
eat_cnt = 0

while True:
    fy, fx, d = bfs(shark_y, shark_x, size)
    if d == -1:                      # 더 먹을 물고기 없음
        break

    t += d
    eat_cnt += 1
    maps[shark_y][shark_x]=0
    maps[fy][fx] = 9                 # 먹은 칸은 빈칸

    shark_y, shark_x = fy, fx        # 상어 이동

    if eat_cnt == size:              # 크기 증가
        size += 1
        eat_cnt = 0

print(t)
