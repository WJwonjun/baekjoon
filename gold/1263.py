import sys
input = sys.stdin.readline
N = int(input())
nums = []

for _ in range(N):
    T,S = map(int,input().split())
    nums.append((T,S))
nums.sort(key = lambda x: (x[1],x[0])) #급하고 일찍 끝나는 순 정렬
#start 기준으로 정렬할 경우 시작은 빨리 해야하는데 갭차이 정확하게 반영 불가능
# ex. 지금 5초인데 8초에는 시작해야 하고 10초 걸리는 task랑 9초에는 시작해야 하고 2초 걸리는 task 중 앞에걸 먼저 실행해버림
# (10,8):(2,9) vs (10,18):(2,11) 후자가 맞음
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