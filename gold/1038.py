import sys
from collections import defaultdict
N = int(input())
nums=[]



for i in range(0,10):
    stack=[i]
    cnt=0
    while stack and cnt<10:
        cur = stack.pop()
        nums.append(cur)
        
        for j in range(cur%10):
            stack.append(int(cur*10+j))
    
        



        #print(i,cur,nums,stack)
nums.sort()
if N<len(nums):
    print(nums[N])
else:
    print(-1)
    

# 전체 개수(1023개)를 고려하면 어렵지 않은 문제.
# 구현보다 먼저 수학적으로 고려해 보는 습관 가지자. -> 조합 / 개수
