import sys
input = sys.stdin.readline
N = int(input())
paper = []
paper = [list(map(int, input().split())) for _ in range(N)]


white = 0
blue = 0

def check(sr, sc, size):
    global white, blue
    
    first = paper[sr][sc]
    same = True
    
    for i in range(sr, sr + size):
        for j in range(sc, sc + size):
            if paper[i][j] != first:
                same = False
                break
        if not same:
            break
    
    if same:
        if first == 0:
            white += 1
        else:
            blue += 1
        return
    
    half = size // 2
    check(sr, sc, half)                 # 좌상
    check(sr, sc + half, half)          # 우상
    check(sr + half, sc, half)          # 좌하
    check(sr + half, sc + half, half)

check(0,0, N)
print(white)
print(blue)