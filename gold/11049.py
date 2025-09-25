import sys,heapq

input = sys.stdin.readline

N = int(input())
maps =[]
for i in range(N):
    x,y = map(int,input().split())
    heapq.heappush(maps, (-x,-y,0))

while maps:
    cur = heapq.heappop(maps)
    print(cur)