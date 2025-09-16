import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 부분합 전부 구하기
subA = []
for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        subA.append(s)

subB = []
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        subB.append(s)

# subA의 빈도 저장
countA = Counter(subA)
countB = Counter(subB)
# 정답 세기
answer = 0
for a,freqA in countA.items():
    target = T-a
    if target in countB:
        answer+=freqA*countB[target]
print(answer)
