import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
N,M,X = map(int, input().split())
route = defaultdict(list)
route2 = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    route[b].append((a, c))
    route2[a].append((b, c))

dist = [float('inf')] * (N + 1)
dist[X] = 0
heap = [(0,X)]

while heap:
    d, node = heapq.heappop(heap)
    if dist[node] < d:
        continue
    for next_node, cost in route[node]:
        if dist[next_node] > d + cost:
            dist[next_node] = d + cost
            heapq.heappush(heap, (dist[next_node], next_node))
            
############################################

heap2 = [(0, X)]
dist2 = [float('inf')] * (N + 1)
dist2[X] = 0

while heap2:
    d, node = heapq.heappop(heap2)
    if dist2[node] < d:
        continue
    for next_node, cost in route2[node]:
        if dist2[next_node] > d + cost:
            dist2[next_node] = d + cost
            heapq.heappush(heap2, (dist2[next_node], next_node))

print(max(dist[i] + dist2[i] for i in range(1, N + 1)))