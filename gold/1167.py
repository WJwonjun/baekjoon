import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
trees = defaultdict(list)
for i in range(N):
    nums = list(map(int,input().split()))
    u = nums[0]
    nums = nums[1:-1]
    edges = [(nums[2*j],nums[2*j+1]) for j in range(len(nums)//2)]
    for edge in edges:
        trees[u].append(edge)
        trees[edge[0]].append((u,edge[1])) 
   
    
q = deque([1])
dist = [-1]*(N+1)
dist[1]=0

while q:
    cur = q.popleft()
    for node, distance in trees[cur]:
        if dist[node]==-1:
            dist[node] = dist[cur]+distance
            q.append(node)
u = dist.index(max(dist[1:]))

q = deque([u])
dist = [-1]*(N+1)
dist[u]=0

while q:
    cur = q.popleft()
    for node, distance in trees[cur]:
        if dist[node]==-1:
            dist[node] = dist[cur]+distance
            q.append(node)
u = dist.index(max(dist[1:]))

print(max(dist[1:]))
