import sys
input = sys.stdin.readline

C, N = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**15
dp = [0] + [INF] * C  # dp[j]: j명을 '이상' 모으는 최소비용

for cost, cust in items:
    for j in range(1, C + 1):
        prev = j - cust
        if prev < 0:
            prev = 0
        if dp[prev] + cost < dp[j]:
            dp[j] = dp[prev] + cost
        print(dp[j])

print(dp[C])