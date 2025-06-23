import sys
input = sys.stdin.read
    
data = list(map(int,input().split()))
N = data[0]
stack=[]

ans = data[1:] #12 5 78 6 34
op=[]
count=1
temp = True
for i in range(N):
    while count <= ans[i]:
        stack.append(count)
        count+=1
        op.append('+')
        
    if len(stack)!=0 and stack[-1]==ans[i]:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break
if temp:
    for i in op:
        print(i)
else:
    print('NO')
        

    
