import sys
input = sys.stdin.readline
N,M = map(int,input().split())
univ = [list(input().strip()) for rows in range(N)]

count = 0
stack = []
for i in range(N):
    for j in range(M):
        if univ[i][j]=='I':
            stack.append((i,j))


while stack:
    x,y = stack.pop()
    univ[x][y]='X'
    if x>0:
        if univ[x-1][y]=='O':
            stack.append((x-1,y))
            univ[x-1][y]='X'
        elif univ[x-1][y]=='P':
            stack.append((x-1,y))
            univ[x-1][y]='X'
            count+=1

    if y>0:
            if univ[x][y-1]=='O':
                stack.append((x,y-1))
                univ[x][y-1]='X'
            elif univ[x][y-1]=='P':
                stack.append((x,y-1))
                univ[x][y-1]='X'
                count+=1
                
    if x<N-1:
        if univ[x+1][y]=='O':
            stack.append((x+1,y))
            univ[x+1][y]='X'
        elif univ[x+1][y]=='P':
            stack.append((x+1,y))
            univ[x+1][y]='X'
            count+=1
    
    if y<M-1:
        if univ[x][y+1]=='O':
            stack.append((x,y+1))
            univ[x][y+1]='X'
        elif univ[x][y+1]=='P':
            stack.append((x,y+1))
            univ[x][y+1]='X'
            count+=1
        
print(count if count>0 else 'TT')