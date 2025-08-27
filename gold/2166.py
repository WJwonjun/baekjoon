import sys
input = sys.stdin.readline
N = int(input())
x,y = [],[]
for _ in range(N):
    curx,cury = map(int,input().split())
    x.append(curx)
    y.append(cury)
x.append(x[0])
y.append(y[0])

front = 0
back = 0
for i in range(0,N):
    front+=(x[i]*y[i+1])
    back+=(x[i+1]*y[i])
print(round(abs(front-back)*0.5,1))