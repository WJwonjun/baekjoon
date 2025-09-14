import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    maps = {i:[] for i in range(1,N+1)}
    costs = [0] + [int(x) for x in input().split()]
    in_degree = [0]*(N+1)
    for i in range(K):
        x,y = map(int,input().split())
        in_degree[y]+=1
        maps[x].append(y)

    W = int(input())
    #print(maps,costs,in_degree,W)

    dp = [0]*(N+1)
    Q = deque()
    for i in range(1,N+1):
        if in_degree[i]==0:
            Q.append(i)
            dp[i]=costs[i]

    while Q:
        cur = Q.popleft()
        for next in maps[cur]:
            dp[next] = max(dp[next],dp[cur]+costs[next])
            in_degree[next]-=1
            if in_degree[next]==0:
                Q.append(next)
    print(dp[W])
 
"""
위상 정렬 : 그래프 배열 
진입 차수(in_degree) 개념 이용 
1. 진입 차수 계산
2. 큐에 삽입
3. 정렬 실행 -> 여기선 dp
4. in_degree 재계산 -> append
"""