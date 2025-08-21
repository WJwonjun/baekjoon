import sys, heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

maps = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    x,y,cost = map(int, input().split())
    maps[x].append((y, cost))

x, y = map(int, input().split())

heap = [(0, x)]
dist = [float('inf')] * (N + 1)
dist[x] = 0
route = [[] for _ in range(N + 1)]
route[x].append(x)

while heap:
    # print(route[y])
    d, node = heapq.heappop(heap)
    if dist[node] < d:
        continue
    for next_node, cost in maps[node]:
        if dist[next_node] > d + cost:
            dist[next_node] = d + cost
            route[next_node] = route[node] + [next_node]
            heapq.heappush(heap, (dist[next_node], next_node))

print(dist[y])
print(len(route[y]))
print(*route[y]) 