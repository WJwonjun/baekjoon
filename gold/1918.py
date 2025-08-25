import sys
string = list(sys.stdin.readline().strip())
stack=[]

ans=''

special = ['+','-','*','/','(',')']
for c in string:
    if c not in special:
        ans+=c
    else:
        if c=='(':
            stack.append(c)
        elif c==')':
            while stack and stack[-1]!='(':
                ans+=stack.pop()
            stack.pop()
        elif c=='*' or c=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                ans+=stack.pop()
            stack.append(c)
        else:
            while stack and stack[-1]!='(':
                ans+=stack.pop()
            stack.append(c)
        
while stack:
    ans+=stack.pop()

print(ans) 

