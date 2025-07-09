import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start,end):
    dist = [sys.maxsize]*(N+1)
    dist[start]=0
    heap=[(0,start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if dist[node]<cost:
            continue
        
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost<dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap,(new_cost,neighbor))
    return dist[end]

print(dijkstra(start,end))