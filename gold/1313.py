import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
cur = max(nums)
prime = [True]*(cur+1)
prime[1] = False

sum_prime = [-1]

for i in range(2,cur):
    j=2
    while j*i<=cur:
        prime[i*j] = False
        j+=1

while cur>=100:
    if not prime[cur]:
        curstr = str(cur)
        length = len(curstr)
        flag = 0
        for l in range(2,length):
            for s in range(0,length-l+1):
                if not prime[int(curstr[s:s+l])]:
                    flag = 1
                    break
            if flag==1:
                break
        else:
            sum_prime.append(cur)
    cur-=1

sum_prime.sort()
#print(sum_prime)
for num in nums:
    if num in sum_prime:
        print(num)
    else:
        print(sum_prime[bisect_left(sum_prime,num)-1])