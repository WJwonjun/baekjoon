# import sys
# sys.setrecursionlimit(10**6)

# MOD = 1_000_000_007
# N = int(sys.stdin.readline())

# def fib(n):
#     if n==0:
#         return (0,1)

#     a, b = fib(n//2) # a=fib(n//2),b = fib(n//2+1)

#     F_2k = a*((2*b-a)%MOD)%MOD # k=n//2
#     F_2k_1 = (a*a+b*b)%MOD
#     if n%2==1:
#         return (F_2k_1,(F_2k+F_2k_1)%MOD)
#     else:
#         return (F_2k,F_2k_1)

# print(fib(N)[0])

# 재귀 횟수만큼 메모리 사용하므로 오류 발생

# import sys
# sys.setrecursionlimit(10**6)

# MOD = 1_000_000_007
# N = int(sys.stdin.readline())

# def fib(n):
#     # (F(n), F(n+1)) mod MOD
#     if n == 0:
#         return (0, 1)
#     a, b = fib(n >> 1)          # (F(k), F(k+1)), k = n//2
#     t = (2*b - a) % MOD
#     c = (a * t) % MOD           # F(2k)
#     d = (a*a + b*b) % MOD       # F(2k+1)
#     if n & 1:                   # n 홀수
#         return (d, (c + d) % MOD)
#     else:                       # n 짝수
#         return (c, d)

# print(fib(N)[0])


import sys
MOD = 1_000_000_007

n = int(sys.stdin.readline())

def fib_fast_iter(n: int) -> int:
    # (F(k), F(k+1))를 (a,b)에 유지
    a, b = 0, 1  # F(0)=0, F(1)=1
    if n == 0:
        return 0
    # n의 최상위 비트부터 내려오며 doubling
    for i in range(n.bit_length() - 1, -1, -1):
        # 현재 (a,b) = (F(k), F(k+1)) 에서 (F(2k), F(2k+1)) 계산
        t = (2*b - a) % MOD
        c = (a * t) % MOD          # F(2k)
        d = (a*a + b*b) % MOD      # F(2k+1)
        if (n >> i) & 1:           # 다음 비트가 1이면 k -> 2k+1
            a, b = d, (c + d) % MOD
        else:                      # 0이면 k -> 2k
            a, b = c, d
    return a

print(fib_fast_iter(n))

#반복으로 풀면 O(1) 만큼만 메모리 사용
