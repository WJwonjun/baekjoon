import sys,heapq
from collections import defaultdict
V,E = map(int,input().split())

node = defaultdict(list)
for _ in range(E):
    x,y,c = map(int,input().split())
    node[x].append((y,c))
    node[y].append((x,c))


visited = [int(1e6)]*(V+1)



Q = [(0,1)]

while Q:
    cost, next = heapq.heappop(Q)
    if visited[next]<cost:
        continue

    visited[next] = cost
    for neighbor,cost in node[next]:
        if visited[neighbor]==int(1e6):
            heapq.heappush(Q,(cost,neighbor))

print(sum(visited[1:]))
    



