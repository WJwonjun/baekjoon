import sys
sys.setrecursionlimit(10**9)
N, S = map(int, input().split())
nums = list(map(int,input().split()))

i,j = 0,-1
tmp=0
min_len = int(1e9)




while True:
    if tmp<S:
        if j==N-1:
            break
        else:
            j+=1
            tmp+=nums[j]
    
  
    else:
            i+=1
            tmp-=nums[i-1]
    
    if j-i+1<min_len and tmp>=S:
        min_len = j-i+1


print(min_len if min_len!=int(1e9) else 0)