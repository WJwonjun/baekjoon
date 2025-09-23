import sys
from collections import deque
N,M = map(int,input().split())

in_degree = [0]*(N+1)
child = {i:set() for i in range(1,N+1)}

for i in range(M):
    nums = list(map(int,input().split()))
    for j in range(1,nums[0]+1):
        for k in range(j+1,nums[0]+1):
            if nums[k] not in child[nums[j]]:
                child[nums[j]].add(nums[k])
                in_degree[nums[k]]+=1
# print(child)
# print(in_degree)

Q = deque([])
for i in range(1,N+1):
    if in_degree[i]==0:
        Q.append(i)

ans = []
while Q:
    cur = Q.popleft()
    ans.append(cur)

    for sib in child[cur]:
        in_degree[sib]-=1
        if in_degree[sib]==0:
            Q.append(sib)

if len(ans)!=N:
    print(0)
else:
    for i in range(len(ans)):
        print(ans[i])