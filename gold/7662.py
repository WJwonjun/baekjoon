from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    min_h,max_h = [],[]
    count = defaultdict(int)
    for _ in range(N):
        cmd, N = input().split()
        N = int(N)
        if cmd=='I':
            heapq.heappush(min_h,N)
            heapq.heappush(max_h,-N)
            count[N]+=1
        elif cmd=='D':
            if N==1:
                while max_h:
                    top = -heapq.heappop(max_h)
                    if count[top]>0:
                        count[top]-=1
                        break
            else:
                while min_h:
                    top = heapq.heappop(min_h)
                    if count[top]>0:
                        count[top]-=1
                        break
    while min_h and count[min_h[0]]==0:
        heapq.heappop(min_h)
    while max_h and count[-max_h[0]]==0:
        heapq.heappop(max_h)
    if not min_h or not max_h:
        print('EMPTY')
    else:
        print(-max_h[0],min_h[0])