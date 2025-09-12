import sys
input = sys.stdin.readline
N,M = map(int, input().split())


parent = [i for i in range(N)]

def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return False
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
    return True

for i in range(M):
    x,y = map(int,input().split())

    if not union(x,y):
        print(i+1)
        break
    



else:
    print(0)
