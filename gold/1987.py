import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [False] * 26
max_len = 0

def dfs(x,y,count):
    global max_len
    max_len = max(max_len,count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < R and 0 <= ny < C:
            alpha = ord(board[nx][ny]) - ord('A')
            if not visited[alpha]:
                visited[alpha]= True
                dfs(nx,ny,count+1)
                visited[alpha]= False

visited[ord(board[0][0]) - ord('A')] = True
dfs(0,0,1)
print(max_len)

