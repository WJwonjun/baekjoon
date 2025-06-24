N,M = map(int,input().split())
D = dict()
for i in range(N):
    info = list(input().split())
    D[info[0]] = info[1]
for j in range(M):
    search = input()
    print(D[search])
    