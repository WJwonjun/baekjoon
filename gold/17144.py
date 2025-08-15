import sys

input = sys.stdin.readline
R,C,T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
for i in range(R):
    if maps[i][0] == -1:
        cleaner.append(i)
upper, lower = cleaner[0], cleaner[1]

def circulate(board):
    # 위쪽(반시계)
    # 위쪽: 위로
    for y in range(upper-1, 0, -1):
        board[y][0] = board[y-1][0]
    # 위쪽: 왼->오 (맨 윗줄) <--
    for x in range(0, C-1):
        board[0][x] = board[0][x+1]
    # 위쪽: 아래로 (오른쪽 열)
    for y in range(0, upper):
        board[y][C-1] = board[y+1][C-1]
    # 위쪽: 오->왼 (upper 줄) -->
    for x in range(C-1, 1, -1):
        board[upper][x] = board[upper][x-1]
    board[upper][1] = 0  # 청정기 바로 오른쪽은 깨끗한 공기

    # 아래쪽(시계)
    # 아래쪽: 아래로
    for y in range(lower+1, R-1):
        board[y][0] = board[y+1][0]
    # 아래쪽: 왼->오 (맨 아랫줄)
    for x in range(0, C-1):
        board[R-1][x] = board[R-1][x+1]
    # 아래쪽: 위로 (오른쪽 열)
    for y in range(R-1, lower, -1):
        board[y][C-1] = board[y-1][C-1]
    # 아래쪽: 오->왼 (lower 줄)
    for x in range(C-1, 1, -1):
        board[lower][x] = board[lower][x-1]
    board[lower][1] = 0  # 청정기 바로 오른쪽은 깨끗한 공기



def diffuse(board):
    tmp = [[0] * C for _ in range(R)]
    tmp[upper][0] = -1
    tmp[lower][0] = -1

    for y in range(R):
        for x in range(C):
            if board[y][x] > 0:
                spread = board[y][x] 
                amt = spread//5
                if amt> 0:
                    spread_count = 0
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] != -1:
                            tmp[ny][nx] += amt
                            spread_count += 1
                    tmp[y][x] += (spread - (amt * spread_count))
                else:
                    tmp[y][x] += board[y][x]
    return tmp
 



for _ in range(T):
    maps = diffuse(maps)
    circulate(maps)

result = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] > 0:
            result += maps[i][j]

print(result)

