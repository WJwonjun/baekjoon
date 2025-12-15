import sys
input = sys.stdin.readline

X,Y,W,S = map(int,input().split())

def cal(x1,y1, x2, y2):
    if x2-x1==0 and y2-y1==0:
        return 0
    elif x2-x1==0:
        dy = y2-y1
        return min(dy//2*(S*2)+dy%2*W,dy*W)
    elif y2-y1==0:
        dx = x2-x1
        return min(dx//2*(S*2)+dx%2*W,dx*W)
    elif (x2-x1)==(y2-y1):
        dy = y2-y1
        dx = x2-x1
        return min((dy+dx)*W,dy*S)
    else:
        dy = y2-y1
        dx = x2-x1
        diag = min(dy,dx)
        return min(2*diag*W,diag*S) + cal(x1+diag,y1+diag,x2,y2)

print(cal(0,0,X,Y))