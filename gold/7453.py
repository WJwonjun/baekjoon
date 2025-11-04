import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = [[], [], [], []]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    nums[0].append(a)
    nums[1].append(b)
    nums[2].append(c)
    nums[3].append(d)

ab = []
for a in nums[0]:
    for b in nums[1]:
        ab.append(a + b)

# cd 합의 빈도를 Counter로 저장
cd_counter = Counter()
for c in nums[2]:
    for d in nums[3]:
        cd_counter[c + d] += 1

ans = 0
for s in ab:
    ans += cd_counter[-s]

print(ans)
