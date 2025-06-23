from collections import deque
N, K = map(int, input().split())
nums = deque(i for i in range(1,N+1))
ans = []

while len(nums)>0:
    for i in range(K-1):
        nums.append(nums.popleft())
    ans.append(nums.popleft())
print("<" + ", ".join(map(str,ans)) + ">")
    
