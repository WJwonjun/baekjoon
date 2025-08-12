from collections import deque
N, K = map(int,input().split())

Q = deque([(N,0)])
visited = [-1]*100001
visited[N]=0
flag=0
count=0
while Q:
    cur, time = Q.popleft()
    if cur ==K:
        if flag==0:
            flag=1
            mintime = time
        else:
            if time>mintime:
                break
        count+=1

    if flag==0:    
        for next in (cur+1,cur-1,cur*2):
            if 0<=next<=100000 and (visited[next]==-1 or visited[next]==time+1):
                visited[next] = time+1
                Q.append((next,time+1))

print(mintime)
print(count)