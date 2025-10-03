N, K = map(int, input().split())

if N <= K:  # 이미 물병 개수가 조건 이하
    print(0)
else:
    cnt = 0
    while bin(N).count("1") > K: # 이진수 -> 자동으로 더해주는 효과
        # 가장 작은 1의 자리 물병을 하나 더 산다고 생각
        add = (N & -N)  # N에서 가장 작은 2^k 값
        N += add
        cnt += add
    print(cnt)
