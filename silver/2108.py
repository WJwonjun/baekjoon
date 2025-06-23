import sys
input = sys.stdin.read
data=list(map(int,input().split()))
N = data[0]
nums = sorted(data[1:])

count = [0]*8001
for num in nums:
    count[num+4000]+=1
    

if sum(nums)>=0:
    print(int(sum(nums)/len(nums)+0.5))
else:
    print(int(sum(nums)/len(nums)-0.5))

print(nums[len(nums)//2])

max_num = max(count)
tmp = sorted([idx for idx,num in enumerate(count) if num==max_num])
if len(tmp)>1:
    print(tmp[1]-4000)
else:
    print(tmp[0]-4000)

print(nums[-1]-nums[0])

