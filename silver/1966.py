from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    M, seq = map(int, input().split())
    data=list(map(int, input().split()))
    Q = deque([x,1] if idx==seq else [x,0] for idx, x in enumerate(data))
    ans=0
    while True:
        if Q[0][0]==max(doc[0] for doc in Q):
            ans+=1
            if Q[0][1]==1:
                print(ans)
                break
            else:
                Q.popleft()
        else:
            Q.append(Q.popleft())