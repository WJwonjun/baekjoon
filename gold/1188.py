import math
N,M = map(int,input().split())

cnt = 0

while N>0 and M>1:
    if N>=M:
        N=N%M
    else:
        M-=N
        cnt+=N

print(cnt)

"""
11개 18명 
11번 -> 11/18 7/18 각각 11개
7명, 7/18 11개
필요한 건 4/18 7개, 남은 건 7/18 4개
"""