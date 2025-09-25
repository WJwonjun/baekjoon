import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
T = int(input())

def dfs(x): 
    visited[x] = -1
    nxt = nums[x]

    if visited[nxt]==0:
        dfs(nxt)
    elif visited[nxt]==-1:  #새로운 cycle 발견
        cur = nxt
        while True:
            road[cur] = 1
            if cur ==x:
                break
            cur = nums[cur]
    visited[x] = 1


for _ in range(T):  #C
    N = int(input())
    nums = [0]+list(map(int,input().split()))
    visited = [0]*(N+1)
    road = [0]*(N+1)

    for i in range(1,N+1):  # O(N)
        if visited[i]==0:
            dfs(i)
    
    print(N-sum(road))

# 그래프 스케일 탐색 with DFS
# visited -> -1(현재 route), 0(방문한적 없음), 1(이미 cycle 형성함)
#   path 표시할 필요 없이 visited 상태로 표시
# road -> 0(cycle 없음), 1(cycle 있음)

# O(N+N)