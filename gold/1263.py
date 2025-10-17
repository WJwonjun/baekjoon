import sys
input = sys.stdin.readline
N = int(input())
nums = []

for _ in range(N):
    T,S = map(int,input().split())
    nums.append((T,S))
nums.sort(key = lambda x: (x[1],x[0])) #급하고 오래 걸리는 순 정렬
#print(nums)

t=0

while True:
    tmp_t = t
    for i in range(N):
        cost,cutline = nums[i]
        if cutline>=tmp_t+cost:
            tmp_t+=cost
        else:
            print(t-1)
            sys.exit(0)
        #print(cost,cutline,tmp_t)
    t+=1