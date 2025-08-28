import sys
input = sys.stdin.readline
N = int(input())

liquids = list(map(int,input().split()))
for i in range(len(liquids)-1):
    if liquids[i]*liquids[i+1]<0:
        break

neg = list(reversed(liquids[:i+1]))
pos = liquids[i+1:]
k=0
min_num = float('1e9')
if len(neg)>=2:
    min_num = neg[0]+neg[1]
    x,y = neg[1],neg[0]
if len(pos)>=2:
    min_pos = pos[0]+pos[1]
    if abs(min_num)>min_pos:
        min_num = min_pos
        x,y = pos[0],pos[1]


for i in range(len(neg)):
    while k<len(pos)-1:
        if (neg[i]+pos[k])*(neg[i]+pos[k+1])<=0:
            if abs(neg[i]+pos[k])<min_num and abs(neg[i]+pos[k])<abs(neg[i]+pos[k+1]):
                x,y = neg[i],pos[k]
                min_num = abs(neg[i]+pos[k])
            elif abs(neg[i]+pos[k+1])<min_num and abs(neg[i]+pos[k+1])<abs(neg[i]+pos[k]):
                x,y = neg[i],pos[k+1]
                min_num = abs(neg[i]+pos[k+1])
            
            break
        k+=1
    
    else:
        if abs(neg[i]+pos[k])<abs(min_num):
            x,y = neg[i],pos[k]
            min_num = abs(neg[i]+pos[k])
print(x,y)