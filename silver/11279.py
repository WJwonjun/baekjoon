import sys
import heapq
data = sys.stdin.read().split()
N = int(data[0])
nums = list(map(int,data[1:]))

max_heap = []

for num in nums:
    if num==0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(max_heap,(-num,num))