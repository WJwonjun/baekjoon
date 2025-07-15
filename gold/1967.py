import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    p,c,w = map(int,input().split())
    tree[p].append((c,w))
    tree[c].append((p,w))

def bfs(start):
    visited = [-1]*(N+1)
    visited[start]=0
    Q = deque([start])
    
    while Q:
        cur = Q.popleft()
        for next, next_w in tree[cur]:
            if visited[next]==-1:
                Q.append(next)
                visited[next]= visited[cur]+next_w
    m = max(visited)
    return [visited.index(m),m]

left_long,m1 = bfs(1)
rigght_long,m2 = bfs(left_long)

print(m2)