import sys
input = sys.stdin.readline
N = int(input())
total=0

def inv(n):
    return pow(n,1000000005,1000000007)

for _ in range(N):
    n,s = map(int,input().split())
    inv_n = inv(n)
    total = (total+s*inv_n) % 1000000007
print(total)