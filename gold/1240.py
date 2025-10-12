import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
tree = {i+1:[] for i in range(N)}

for _ in range(N-1):
    x,y,c = map(int,input().split())
    tree[x].append((c,y))
    tree[y].append((c,x))

#print(tree)

for _ in range(M):
    x,y = map(int,input().split())
    Q = deque([(0,x)])
    visited = [False]*(N+1)
    visited[x] = True
    while Q:
        cost,cur = Q.popleft()
        if cur==y:
            print(cost)
            break
        
        for c,neighbor in tree[cur]:
            if visited[neighbor]==False:
                Q.append((c+cost,neighbor))
                visited[neighbor]=True

#그냥 bfs로 풀면 될듯?-> 메모리 초과 -> visited로 해결