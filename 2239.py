import sys
input = sys.stdin.readline
maps = [list(map(int,input().strip())) for _ in range(9)]

indexes = []

for i in range(9):
    for j in range(9):
        if maps[i][j]==0:
            indexes.append((i,j))

idx=0
while 0<=idx<len(indexes):
    y,x = indexes[idx]
    y_box = y//3*3
    x_box = x//3*3

    column = [row[x] for row in maps]

    flat_list = [
    num
    for row in maps[y_box:y_box+3]
    for num in row[x_box:x_box+3]
]
    forbidden = set(maps[y]+column+flat_list)

    for i in range(maps[y][x]+1,10):
        if i not in forbidden:
            maps[y][x]=i
            idx+=1
            break
    else:
        maps[y][x]=0
        idx-=1


for i in range(9):
    print(*maps[i],sep="")