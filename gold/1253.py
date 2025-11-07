import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
c = Counter(nums)
origin = set(nums)
good = set()
ans = 0
for x in range(N):
    for y in range(N):
        if x!=y:
            target = nums[x]+nums[y]
            #print(target)
            if target in origin:
                if target not in good:
                    
                    
                    if nums[x]==0 and nums[y]!=0:
                        if c[nums[y]]>=2:
                            ans+= c[target]
                            good.add(target)

                    elif nums[x]!=0 and nums[y]==0:
                        if c[nums[x]]>=2:
                            ans+= c[target]
                            good.add(target)

                    elif nums[x]==0 and nums[y]==0:
                        if c[0]>=3:
                            ans+= c[target]
                            good.add(target)

                    else:
                        ans+= c[target]
                        good.add(target)
                    
                    #print(target,ans)

print(ans)