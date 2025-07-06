import sys
from collections import deque

input = sys.stdin.readline

A,B,C = map(int,input().split())


def solve(A,B,C):
    if B==1:
        return A%C

    else:
        k = solve(A,B//2,C)
        if B%2==1:
            return (k*k*A)%C
        else:
            return (k*k)%C

print(solve(A,B,C))
    