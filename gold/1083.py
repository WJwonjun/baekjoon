import sys
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
    
    nums = nums[:i] + [target] + nums[i:idx]+nums[idx+1:]
    S-=(idx-i)
    #print(S,i,idx,nums)


print(*nums)


# 사전식 -> greedy가 DP 등보다 효율적 -> 우선순위의 규칙이 그리디로 만들 수 있는 것이 명확