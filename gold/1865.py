import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    route = []
    warmhole = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        route.append((S, E, T))
        route.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        warmhole.append((S, E, -T))
    
    dist = [0] * (N + 1)

    for _ in range(N-1):
            updated=False
            for S,E,T in route + warmhole:
                if dist[E] > dist[S] + T:
                    dist[E] = dist[S] + T
                    updated = True
            if not updated:
                break
        
    for S,E,T in route + warmhole:
            if dist[E] > dist[S] + T:
                print("YES")
                break
    else:
        print("NO")

    
        