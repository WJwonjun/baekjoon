import sys
from collections import deque
N = int(input())
nums = list(map(int,input().split()))
K = int(input())

def find_leaf(tree):
    s = set(tree)
    cnt=0
    for i in range(len(tree)):
        if i not in s and nums[i]!=-2:
            cnt+=1
    
    return cnt



Q = deque([K])
nums[K]=-2

while Q:
    cur = Q.popleft()
    for i in range(len(nums)):
        if nums[i]==cur:
            Q.append(i)
            nums[i]=-2

print(find_leaf(nums))