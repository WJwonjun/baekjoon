total_num = int(input())
nums = list(map(int,input().split()))
ans = 0
tmp=0
for num in nums:
    for i in range(1,num+1):
        if num%i==0:
            tmp+=1
    if tmp==2:
        ans+=1
    tmp=0

print(ans)