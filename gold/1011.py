import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    d = y - x  # 총 이동해야 하는 거리
    
    k = int(math.sqrt(d))

    if d==k*k:
        print(2*k-1)
    elif k*k<d<=k*(k+1):
        print(2*k)
    else:
        print(2*k+1)
    
