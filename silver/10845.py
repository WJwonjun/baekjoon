from collections import deque
import sys
N = int(sys.stdin.readline())
Q = deque()
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0]=='push':
        Q.append(command[1])
    elif command[0]=='pop':
        if len(Q)>0:
            print(Q.popleft())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(Q))
    elif command[0]=='empty':
        if len(Q)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if len(Q)==0:
            print(-1)
        else:
            print(Q[0])
    elif command[0]=='back':
        if len(Q)==0:
            print(-1)
        else:
            print(Q[-1])
        