import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
trees = []
for _ in range(N):
    trees.append(list(map(int,input().split())))
for i in range(1,N):
    for j in range(len(trees[i])):
        if j==0:
            trees[i][j]=trees[i-1][0]+trees[i][j]
        elif j==len(trees[i])-1:
            trees[i][j]=trees[i-1][j-1]+trees[i][j]
        else:
            trees[i][j]=max(trees[i-1][j-1],trees[i-1][j])+trees[i][j]

print(max(trees[N-1]))