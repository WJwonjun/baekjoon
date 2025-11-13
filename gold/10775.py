import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
G = int(input())
P = int(input())
gates = [i for i in range(G+1)]


def find(gi):
    if gi!=gates[gi]:
        gates[gi] = find(gates[gi])
    return gates[gi]

def union(gi):
    gates[gi] = gates[gi-1]
    

for i in range(P):
    gi = int(input())
    target = find(gi)
    if target==0:
        print(i)
        break

    union(target)
    #print(target,gates)

else:
    print(P)