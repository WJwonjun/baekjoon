N = int(input())

stars = [[' ']*2*N for _ in range(N)]

def recursion(i,j,size):
    if size ==3:
        stars[i][j]='*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2,3):
            stars[i+2][j+k]="*"
    else:
        newsize = size//2
        recursion(i,j,newsize)
        recursion(i+newsize,j-newsize,newsize)
        recursion(i+newsize,j+newsize,newsize)
recursion(0,N-1,N)
for star in stars:
    print("".join(star))