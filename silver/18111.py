import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())

ground = [list(map(int,input().split())) for _ in range(N)]


idx  =0
answer = sys.maxsize

for floor in range(257):
    exceed, lack = 0,0
    
    for i in range(N):
        for j in range(M):
            if ground[i][j]>floor:
                exceed += ground[i][j]-floor
            else:
                lack += floor - ground[i][j]
    if exceed+B>=lack:
        if (exceed*2)+lack<=answer:
            answer = (exceed*2)+lack
            idx = floor
                
print(answer,idx)