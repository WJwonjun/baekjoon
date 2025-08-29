import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,R,Q = map(int,input().split(' '))

connect = defaultdict(list)
parent = [-1]*(N+1)
child = defaultdict(list)


def makeTree(currentNode, par):
    for node in connect[currentNode]:
        if node!= par:
            child[currentNode].append(node)
            parent[node] = currentNode
            makeTree(node,currentNode)


for _ in range(N-1):
    x,y = map(int,input().split())

    connect[y].append(x)
    connect[x].append(y)


makeTree(R,-1)

size = [0]*(N+1)

def countsubtree(currentNode):
    size[currentNode] = 1
    for node in child[currentNode]:
        countsubtree(node)
        size[currentNode] += size[node] 


countsubtree(R)




for _ in range(Q):
    q = int(input())
    print(size[q])