import sys
import itertools
input = sys.stdin.readline
N = int(input())

nums = list(map(int,input().split()))
# 50을 만들 수 있는 쌍의 개수
#8개밖에 안되니까 brute force? 2^8 / 2 -> 2^7
all_permutations = list(itertools.permutations(nums))
min_num = '0'*(N-1)+'1'
max_num = '1'*N
#print(min_num,max_num)

max_cnt = 0
for p in all_permutations:
    nums = list(p)
    cnt=0
    temp =[]
    now = 0
    for num in nums:
        now +=num
        temp.append(now)
    
    for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
            if temp[i]+50 ==temp[j]:
                cnt+=1
    
    max_cnt = max(cnt,max_cnt)
print(max_cnt)