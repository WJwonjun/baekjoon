import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = [[False]*M for _ in range(N)]

for i in range(N):
    cards = list(map(int,input().split()))
    for j in range(M):
        nums[i][j] = (cards[j]>0)
#print(nums)


# 그냥 50번 -> joker의 경우의 수
# 최대 N-1번 이동

    # 일단 자원 2개 이상 들고 있으면 무조건 움직여야함
    # 똑같은 자원 1개 들고있는 놈이 여러명이면 한명은 움직여야함 

ans = 50
for i in range(N):
    cnt=0
    ones = set()
    for j in range(N):
        if j==i:
            continue

        if sum(nums[j])>=2:
            cnt+=1

        elif sum(nums[j])==1:
            idx = nums[j].index(True)
            if idx in ones:
                cnt+=1
            else:
                ones.add(idx)

    #print(cnt)

    ans = min(ans,cnt)

print(ans)