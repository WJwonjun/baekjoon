import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  # 문제 보장: 오름차순 정렬

i, j = 0, N - 1
best = 10**19
ansL, ansR = A[i], A[j]

while i < j:
    s = A[i] + A[j]
    if abs(s) < best:
        best = abs(s)
        ansL, ansR = A[i], A[j]
        if best == 0:  # 더 좋아질 수 없음
            break
    if s < 0:
        i += 1   # 합이 음수면 더 크게(오른쪽) 이동
    else:
        j -= 1   # 합이 양수면 더 작게(왼쪽) 이동

print(ansL, ansR)
