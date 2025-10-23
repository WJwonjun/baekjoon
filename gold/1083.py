import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
S = min(N*(N-1)/2,int(input()))




for i in range(N):
    if S==0:
        break

    ran = min(N-i-1,S)
    target = max(nums[i:i+ran+1])
    idx = nums.index(target)
    if i==idx:
        continue
    for j in range(idx,i,-1):
        nums[j],nums[j-1] = nums[j-1],nums[j]
    S-=(idx-i)
    #print(S,i,idx,nums)


print(*nums)