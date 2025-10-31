import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
broke = set(map(int,input().split()))
# 만들 수 있는 제일 가까운 조합 찾기
cand = []
digit = list(map(int,str(N)))

def can_make(num):
    for ch in str(num):
        if int(ch) in broke:
            return False
    return True

answer = abs(N - 100)  
for num in range(1000000):
    if can_make(num):
        # 누를 수 있는 숫자 중 하나
        press_count = len(str(num)) + abs(num - N)  # 숫자 버튼 + 이동
        answer = min(answer, press_count)
print(answer)