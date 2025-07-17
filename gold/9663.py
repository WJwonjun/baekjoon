N = int(input())

visited = [-1]*N
count = 0

def dfs(floor):
    global count
    
    for i in range(N): #가로 하나씩 검사
        flag=0
        for j in range(floor-1,-1,-1): #세로방향 탐색
            if abs(floor-j)==abs(visited[j]-i) or i==visited[j]: # 대각선 겹치는거 하나라도 있으면 탈출
                    flag=1
                    break 
                
        if flag==0 : #대각선 + 세로 조건 검사
            if floor == N-1:
                count+=1
            else:
                visited[floor]=i
                dfs(floor+1) #세로방향 탐색
                visited[floor]=-1

dfs(0)
print(count)