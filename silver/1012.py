T = int(input())
for t in range(T):
    M,N,K = map(int,input().split())
    farm = [[0]*N for _ in range(M)]
    for k in range(K):
        y,x = map(int,input().split())
        farm[y][x]=1
    stack = []
    count=0
    for i in range(M):
        for k in range(N):
            if farm[i][k]==1:
                 count+=1
                 farm[i][k]=0
                 stack.append((i,k))
                 while stack:
                     
                    target = stack.pop()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N and farm[nx][ny] == 1:
                            farm[nx][ny]=0
                            stack.append((nx, ny))
    print(count)
    
                         
      