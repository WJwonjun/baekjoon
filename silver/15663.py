import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
stack = []
used = [False]*N # 7 하나밖에 없는데 7 7과 같은 사례 막음

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return

    last_used = -1  # 1 9 다음 또 1 9 나오는 거 막음
    for i in range(N):
        if not used[i] and last_used != nums[i]:
            used[i] = True
            stack.append(nums[i])
            dfs(depth + 1)
            stack.pop()
            used[i] = False
            last_used = nums[i]

dfs(0)