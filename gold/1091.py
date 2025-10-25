import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))  # i번 카드가 가야할 플레이어 번호
S = list(map(int, input().split()))  # 섞는 방법

# 초기 카드 배열 (0부터 N-1까지)
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
    # 현재 상태가 올바른지 확인
    if check(nums):
        print(cnt)
        break
    
    # 카드 섞기
    nums = shuffle(nums)
    #print(nums)
    cnt += 1
    
    # 원래 상태로 돌아왔다면 불가능
    if nums == origin:
        print(-1)
        break