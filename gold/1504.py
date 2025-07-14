import sys,heapq
from collections import defaultdict
input = sys.stdin.readline

N,E = map(int,input().split())
graph = defaultdict(list)
for i in range(E):
    x,y,cost = map(int,input().split())
    graph[x].append((y,cost))
    graph[y].append((x,cost))
v1,v2 = map(int,input().split())


def dijkstra(start):
    distance = [int(1e9)]*(N+1)
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start]=0
    
    while Q:
        dist,now = heapq.heappop(Q)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))

    return distance

start_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_first = start_distance[v1]+v1_distance[v2]+v2_distance[N]
v2_first = start_distance[v2]+v2_distance[v1]+v1_distance[N]
res = min(v1_first, v2_first)
print(res if res < int(1e9) else -1)
    