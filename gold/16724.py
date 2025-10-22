import sys
input = sys.stdin.readline
N,M = map(int,input().split())

def move(y,x,command):
    if command=='U':
        return (y-1,x)
    elif command=='D':
        return (y+1,x)
    elif command=='L':
        return (y,x-1)
    elif command=='R':
        return (y,x+1)
    
maps = [list(input().strip()) for _ in range(N)]
#print(maps)
visited = [[False]*M for _ in range(N)]


ans=0

for i in range(N):
    for j in range(M):
        if visited[i][j]==False:
            stack = [(i,j)]
            route = {(i,j)}
            visited[i][j]=True
            flag=0
            while stack:
                y,x = stack.pop()
                next_y,next_x = move(y,x,maps[y][x])
                if visited[next_y][next_x]==False :
                    stack.append((next_y,next_x))
                    route.add((next_y,next_x))
                    visited[next_y][next_x]=True
                elif visited[next_y][next_x]==True and (next_y,next_x) in route:
                    ans+=1
                    continue
                elif visited[next_y][next_x]==True and (next_y,next_x) not in route:
                    continue
                #print(y,x,next_y,next_x,ans,visited[y][x],route)

print(ans)