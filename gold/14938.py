import sys
input = sys.stdin.readline
import heapq

n,m,r = map(int, input().split())
items = [0]+list(map(int, input().split())) 
maps = {i:[] for i in range(1, n+1)}
for _ in range(r):
    x,y,d = map(int, input().split())
    maps[x].append((d, y))
    maps[y].append((d, x))
max_items = [0]*(n+1)

for i in range(1, n+1):
    
    heap = [(0,i)]
    visited = [False] * (n + 1)
    while heap:
        dist, current = heapq.heappop(heap)
        if visited[current]:
            continue
        visited[current] = True
        max_items[i] +=items[current]
        for d, next_node in maps[current]:
                if not visited[next_node] and dist + d <= m:
                    heapq.heappush(heap, (dist + d, next_node))

print(max(max_items))
