import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
T = int(input())

def dfs(x):
    visited[x] = -1
    nxt = nums[x]

    if visited[nxt]==0:
        dfs(nxt)
    elif visited[nxt]==-1:
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