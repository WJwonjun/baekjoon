N = int(input())
nums = list(map(int,input().split()))
k= [0]*20000001
for num in nums:
    k[num+1000000]+=1
    
M = int(input())
Ms = list(map(int,input().split()))
for i in Ms:
    print(k[i+1000000],end=' ')
    
    
