from os import times_result
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
events = {}
for _ in range(N+M):
    x,y = map(int,input().split())
    events[x] = y



target = 1
Q= deque([1])
count = 0

visited = [False]*101
visited[1] = True
while Q:
    for _ in range(len(Q)):
        target = Q.popleft()
        for d in range(1,7):
            next = target+d
            if next>100:
                continue
            if next in events :
                next = events[next]
            if not visited[next]:
                if next==100:
                    print(count+1)
                    sys.exit(0)
                Q.append(next)
                visited[next] = True
    count+=1       
    
