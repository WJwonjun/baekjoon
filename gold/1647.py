import sys, heapq
from collections import defaultdict
N, M  = map(int,input().split())
route = defaultdict(list)

for _ in range(M):
    x,y,c = map(int,input().split())
    route[x].append((c,y))
    route[y].append((c,x))



visited = [int(1e6)]*(N+1)
Q = [(0,1)]

while Q:
    cost, next = heapq.heappop(Q)
    if visited[next]<cost:
        continue
    
    visited[next] = cost
    for cost, neighbor in route[next]:
        if visited[neighbor]==int(1e6):
            heapq.heappush(Q,(cost, neighbor))

print(sum(visited[1:])-max(visited[1:]))