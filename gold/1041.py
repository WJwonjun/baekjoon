## 1: (n-2)*(n-1)*4 + (n-2)*(n-2) = 4*(n2-3n+2) + n2-4n+4  = 5n2-16n+12 -> 
## 2: (n-1)*4+(n-2)*4 = 8n-12 -> 16n-24  
## 3: 4                                12    
# 
#               
import sys


N = int(input())
nums = list(map(int,sys.stdin.readline().split()))

small_1 = min(nums)
small_2 = 150
for i in range(0,6):
    for j in range(i+1,6):
        if i+j!=5:
            small_2 = min(nums[i]+nums[j],small_2)

small_3_indexes = [(0,3,4),(0,1,3),(0,1,2),(0,2,4),(5,3,4),(5,1,3),(5,1,2),(5,2,4)]
small_3 = 200
for idx_group in small_3_indexes:
    group_sum = sum(nums[i] for i in idx_group)  # 해당 인덱스 값들의 합
    small_3 = min(small_3, group_sum)

#print(small_1,small_2,small_3)
if N==1:
    print(sum(nums)-max(nums))
elif N==2:
    print(small_2*4+small_3*4)

else:
    print(small_1*(5*(N**2)-16*N+12)+small_2*(8*N-12)+small_3*4)

