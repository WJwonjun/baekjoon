import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            houses.append((y, x))
        elif maps[y][x] == 2:
            chickens.append((y, x))

min_total = float('inf')

for selected in combinations(chickens, M):
    total = 0
    for hy, hx in houses:
        dist = min(abs(hy - cy) + abs(hx - cx) for cy, cx in selected)
        total += dist
    min_total = min(min_total, total)
    
print(min_total)