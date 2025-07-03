import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
stack = []

def dfs(start,depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(start,N):
            if nums[i] not in stack:
                stack.append(nums[i])
                dfs(0,depth+1)
                stack.pop()



dfs(0,0)