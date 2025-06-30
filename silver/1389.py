import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
dic = {i+1:[] for i in range(N)}
for _ in range(M):
    x,y = map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)

min_kevin = sys.maxsize
answer = 0

for i in range(1,N+1):
    visited = [False]*(N+1)
    distance = [0]*(N+1)
    Q = deque([i])
    visited[i] = True
    
    while Q:
        now = Q.popleft()
        for neighbor in dic[now]:
            if not visited[neighbor]:
                visited[neighbor]=True
                distance[neighbor] = distance[now]+1
                Q.append(neighbor)
    total = sum(distance[1:])
    if total<min_kevin:
        min_kevin=total
        answer=i             
print(answer)
                        