import sys
data = list(map(int,sys.stdin.read().split()))
N = data[0]
nums = [(i+1,num) for i,num in enumerate(data[1:])]
nums.sort(key = lambda x: x[1])
result = [0]*(N)

count = 0
current = nums[0][1]


for i in range(0,N):
    seq, num = nums[i][0],nums[i][1]
    
    if num>current:
        current = num
        count+=1
        
    result[seq-1]=count
    
print(" ".join(map(str,result)))
