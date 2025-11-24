import sys
from collections import Counter
input = sys.stdin.readline

N=  int(input())
for i in range(N):
    sol = list(map(int,input().split()))
    counter = Counter(sol[1:])
    for key in counter:
        if counter[key]>(sol[0]/2):
            print(key)
            break
    else:
        print("SYJKGW")