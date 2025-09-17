import sys
from collections import deque

N, M = map(int, input().split())
Q = deque()
topo = {i:0 for i in range(1,N+1)}
graph = {i:[] for i in range(1,N+1)}

for _ in range(M):
    i, j = map(int, input().split())

    graph[j].append(i)
    topo[i]+=1


for i in range(1,N+1):
    if topo[i]==0:
        Q.append(i)
ans = []
while Q:
    cur = Q.popleft()
    for neighbor in graph[cur]:
        topo[neighbor]-=1
        if topo[neighbor]==0:
            Q.append(neighbor)

    ans.append(cur)
print(*list(reversed(ans)))



"""
# DAG(directed acyclic Graph): 방향 있는 순환 없는 그래프 
 - 주로 "어떤 것이 먼저 와야 한다"라는 조건 있을 때 사용

# 위상 정렬 : DAG의 모든 노드를 선후 관계를 지키면서 순서대로 나열하는 것. 
 - DAG의 모든 노드를 "선후 관계를 지키면서 순서대로 나열" 하는 것.
 - 말 그대로 위상을 따라 정렬하는 것. 
 - 조건들이 서로 얽혀 있어서 독립적으로 처리 불가능


"""