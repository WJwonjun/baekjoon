N = int(input())
S = list(map(int, input().split()))
max_score = max(S)
new_S = [o_s/max_score*100 for o_s in S]
print(sum(new_S)/N)