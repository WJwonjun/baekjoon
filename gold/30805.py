import sys
N  = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

max_nums = []

for i in range(N):
    pa, pb = i, 0
    last_nums = []
    while True:
        candA = set(A[pa:]) if pa<N else set()
        candB = set(B[pb:]) if pb<M else set()
        common = candA & candB
        if not common:
            break
        v = max(common)

        ia = pa
        while ia < N  and A[ia] !=v:
            ia+=1
        if ia==N:
            break

        jb = pb
        while jb < M and B[jb] != v:
            jb+=1
        if jb==M:
            break
        
        last_nums.append(v)
        pa, pb = ia+1, jb+1

    if last_nums>max_nums:
        max_nums = last_nums

if max_nums:
    print(len(max_nums))
    print(*max_nums)
else:
    print(0)