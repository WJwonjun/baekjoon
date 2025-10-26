import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))  # i번 카드가 가야할 플레이어 번호
S = list(map(int, input().split()))  # 섞는 방법

nums = list(range(N))
origin = nums[:]

def shuffle(nums):
    tmp = [0] * N
    for i in range(N):
        tmp[i] = nums[S[i]]
    return tmp

def check(nums):
    for i in range(N):
        if nums[i]%3!=P[i]:
            return False
    return True

cnt = 0

while True:
    if check(nums):
        print(cnt)
        break
    

    nums = shuffle(nums)
    #print(nums)
    cnt += 1
    
    if nums == origin:
        print(-1)
        break

# 같은 방식으로 순회 -> 반드시 돌아오게 되어있음