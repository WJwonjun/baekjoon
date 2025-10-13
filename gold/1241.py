import sys
from collections import Counter
data = list(map(int,sys.stdin.readlines()))
N = data[0]
nums =data[1:]
big = max(nums)
nums_dict = Counter(nums)
sorted_counter = dict(sorted(nums_dict.items(), key=lambda x: x[0]))
ans = [-1]*(big+1) #N의 약수 몇개인가, down->top 방식이 중복 없을듯

for key in sorted_counter:    #O(N)
    for j in range(1,big//key+1): #O(max(nums))
        if j*key in sorted_counter:
            ans[j*key]+=sorted_counter[key]

for i in range(N):
    print(ans[nums[i]],end='\n')