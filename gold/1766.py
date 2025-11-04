# DAG네 이건
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
info = {i:[] for i in range(1,N+1)}
in_degree = [0]*(N+1)
for _ in range(M):
    y,x = map(int,input().split())
    info[y].append(x)
    in_degree[x]+=1
#print(info)
#print(in_degree)

Q = deque([])
for i in range(1,N+1):
    if in_degree[i]==0:
        Q.append(i)

ans = []
while Q:
    cur = Q.popleft()
    ans.append(cur)
    if info[cur]:
        for n in info[cur]:
            in_degree[n]-=1
            if in_degree[n]==0:
                Q.append(n)
        Q = deque(sorted(Q))

print(*ans)


#Q보다 heap이 나았을듯