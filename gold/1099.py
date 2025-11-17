import sys
from collections import defaultdict
input = sys.stdin.readline

sentence = input().strip()
N = int(input())
L = len(sentence)

# 단어들을 정렬 키로 묶기
words = defaultdict(list)
for _ in range(N):
    w = input().strip()
    key = ''.join(sorted(w))
    words[key].append(w)

dp = [10**9] * (L+1)
dp[0] = 0

for j in range(1, L+1):     # prefix 길이
    cnt = [0]*26            # substring(i:j)의 문자 개수
    for i in range(j-1, -1, -1):   # 시작점 i
        cnt[ord(sentence[i]) - 97] += 1

        # 정렬 키 생성
        key_list = []
        for k in range(26):
            if cnt[k]:
                key_list.append(chr(k + 97) * cnt[k])
        key = ''.join(key_list)

        if key in words:
            substring = sentence[i:j]
            length = j - i

            best = 10**9
            for target in words[key]:
                cost = sum(substring[x] != target[x] for x in range(length))
                if cost < best:
                    best = cost

            dp[j] = min(dp[j], dp[i] + best)

ans = dp[L]
print(ans if ans < 10**9 else -1)
