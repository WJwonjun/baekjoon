import sys
from collections import Counter
input = sys.stdin.readline
N,M = map(int,input().split())
maps = [ input().strip() for _ in range(N)]
K = int(input())
#print(maps)

numcnt = Counter(maps)
numcnt = dict(sorted(numcnt.items(),key = lambda x: -x[1]))
#print(numcnt)

for num in numcnt:
    need=0
    for c in list(num):
        if c=='0':
            need+=1
    #print(num,need)
    if K>=need and (K-need)%2==0:
        print(numcnt[num])
        sys.exit(0) 
print(0)