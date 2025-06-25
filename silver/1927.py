import heapq
import sys
min_heap=[]

T = int(input())
for i in range(T):
    c = int(sys.stdin.readline())
    if c==0:
        if len(min_heap)>0:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap,c)