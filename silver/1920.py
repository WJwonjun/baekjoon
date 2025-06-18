N = int(input())
domain = set(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))
arr = [0]*M
for i in range(M):
    if target[i] in domain:
        arr[i] +=1
for i in range(M):
    print(arr)
