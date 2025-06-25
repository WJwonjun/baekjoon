from collections import deque
N,M,V = map(int,input().split())
dic = {i:[] for i in range(1,N+1)}
for i in range(M):
    x,y = map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)

stack = [V]
visited = []
while stack:
    target = stack.pop()
    if target not in visited:
        visited.append(target)
        
        if len(dic[target])>0:
            for data in sorted(dic[target],reverse=True):
                if data not in visited :
                    stack.append(data)
print(' '.join(map(str,visited)))

Q = deque([V])
visited = []
while Q:
    target = Q.popleft()
    if target not in visited:
        visited.append(target)
        
        if len(dic[target])>0:
            for data in sorted(dic[target]):
                if data not in visited :
                    Q.append(data)

print(' '.join(map(str,visited)))