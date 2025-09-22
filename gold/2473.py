import sys
N = int(input())
nums = list(map(int,input().split()))

nums.sort()
#print(nums)


min_diff = float('inf')
result_idx = []
#print(nums)
for idx in range(len(nums)): #N
    l,r = idx+1, len(nums)-1
    
    while l<r:
        current_sum  = nums[idx]+nums[l]+nums[r]

        if abs(current_sum)<min_diff:
            min_diff = abs(current_sum)
            result_idx = [nums[idx],nums[l],nums[r]]

        if current_sum==0:
            print(*result_idx)
            sys.exit(0)
        elif current_sum<0:
            l+=1
        else:
            r-=1

print(*result_idx)