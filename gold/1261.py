import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input().split())
miro = [list(input().strip()) for _ in range(N)]
count = [[-1]*M for _ in range(N)]


zero_Q = deque([(0,0)])
one_Q = deque([])
count[0][0] = 0

cnt = 0

while zero_Q:
    while zero_Q:
        y,x = zero_Q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny,nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M and count[ny][nx]==-1:
                if miro[ny][nx]=='0':
                    count[ny][nx] = cnt
                    zero_Q.append((ny,nx))
                elif miro[ny][nx]=='1':
                    one_Q.append((ny,nx))
    
    while one_Q:
        y,x = one_Q.popleft()
        if miro[y][x] =='1':
            miro[y][x] = '0'
            zero_Q.append((y,x))
    
    cnt+=1

print(count[N-1][M-1])
"""
0인 부분 다 탐색 
1인 부분 하나씩 부수면서 탐색
"""