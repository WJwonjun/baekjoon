import sys
input = sys.stdin.readline

N, M = map(int,input().split())

stack = []

def dfs(start,depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(start,N+1):
            stack.append(i)
            dfs(i+1,depth+1)
            stack.pop()



dfs(1,0)