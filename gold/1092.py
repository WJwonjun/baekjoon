import sys
input = sys.stdin.readline
N = int(input())
cranes = list(map(int,input().split()))
cranes.sort()

M = int(input())
boxes = list(map(int,input().split()))
boxes.sort()

if max(boxes) > max(cranes):
    print(-1)
    sys.exit(0)

counter = [-1] * N
tmp = -1
for i in range(N):
    while -1 <= tmp <= M-2 and cranes[i] >= boxes[tmp+1]:
        tmp += 1
    counter[i] = tmp

moved = [False] * M
cnt = 0

# 수정: 모든 박스가 옮겨질 때까지
while sum(moved) < M:
    for i in range(N):
        while counter[i] >= 0:
            if not moved[counter[i]]:
                moved[counter[i]] = True
                counter[i] -= 1  # 수정: break 전에 감소
                break
            counter[i] -= 1
    cnt += 1

print(cnt)