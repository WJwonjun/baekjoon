t, N, K, R1, R2, C1, C2 = map(int,input().split())

if t==0:
    print(0)
else:
    for r in range(R1, R2 + 1):
        for c in range(C1, C2 + 1):
            tmp_r, tmp_c = r, c
            flag = 0  # 검은색(1) 판별용

            full_length = N ** t
            size = full_length // N

            # 한 점이 어느 단계의 중앙에 속하는지 체크
            for _ in range(t):
                white = (N - K) // 2

                # 현재 단계에서 중앙 영역에 포함되는 경우
                if white * size <= tmp_r < (white + K) * size and \
                   white * size <= tmp_c < (white + K) * size:
                    print("1", end="")
                    flag = 1
                    break

                # 아니라면, 다음 단계(작은 정사각형 안의 좌표)로 축소
                tmp_r %= size
                tmp_c %= size
                size //= N

            if not flag:
                print("0", end="")
        print()
