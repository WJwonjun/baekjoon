import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
connects = {i:[] for i in range(1,N+1)}

for i in range(M):
    x,y = map(int,input().split())
    connects[x].append(y)
    connects[y].append(x)


visited = [False] * (N + 1)
result = 0

for i in range(1, N + 1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True
        while queue:
            current = queue.popleft()
            for neighbor in connects[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        result += 1

print(result)
        