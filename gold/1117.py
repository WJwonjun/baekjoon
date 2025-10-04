W,H,f,c,x1,y1,x2,y2 = map(int,input().split())
size = W*H
"""
for x in range(x1,x2):
    for y in range(y1,y2):
        size-=(c+1)
        if x<min(f,W-f):    
            size-=(c+1)
"""

size-= (x2-x1)*(y2-y1)*(c+1)


if min(f,W-f)==f and f>x1:
        size-=(min(f,x2)-x1)*(y2-y1)*(c+1)

elif min(f,W-f)==W-f and W-f>x1:
        size-=(min(W-f,x2)-x1)*(y2-y1)*(c+1)
print(size)


        