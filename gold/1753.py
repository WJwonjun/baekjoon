import sys,heapq
from collections import defaultdict
input = sys.stdin.readline


V,E = map(int,input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


def dijkstra(start):
    distance = [int(1e9)]*(V+1)
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start]=0
    
    while Q:
        dis, cur = heapq.heappop(Q)
        
        if dis>distance[cur]:
            continue
    
        for v,w in graph[cur]:
            cost = dis+w
            if cost<distance[v]:
                distance[v]=cost
                heapq.heappush(Q,(cost,v))
    return distance

distance= dijkstra(K)
for i in range(1,V+1):
    print(distance[i] if distance[i]<int(1e9) else 'INF')