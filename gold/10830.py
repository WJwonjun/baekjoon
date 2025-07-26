import sys
input = sys.stdin.readline

N,B=map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]


def matmul(a,b):
    X = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                X[i][j] += a[i][k]*b[k][j]
            X[i][j]%=1000
    return X

def square(x,n):
    if n==1:
        return [[x[i][j] % 1000 for j in range(N)] for i in range(N)]
    temp = square(x,n//2)
    if n%2==0:
        return matmul(temp,temp)
    else:
        return matmul(matmul(temp,temp),x)

result = square(mat,B)

for k in result:
    print(*k)