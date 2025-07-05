import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
stack = []

def dfs(start,depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return

    last_used = -1  # 1 9 다음 또 1 9 나오는 거 막음
    for i in range(start,N):
        if last_used != nums[i]:

            stack.append(nums[i])
            dfs(i,depth + 1)
            stack.pop()
            last_used = nums[i]

dfs(0,0)