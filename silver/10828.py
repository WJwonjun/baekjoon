import sys

N = int(sys.stdin.readline())
stack=[]
for i in range(N):
    full_command = sys.stdin.readline().split()
    command=full_command[0]
    
    if command=='push':
        stack.append(full_command[1])
    elif command == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
