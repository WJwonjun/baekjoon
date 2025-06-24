import sys
data = sys.stdin.read().split()
M,N = int(data[0]),int(data[1])
D=dict()
count = 0
for i in range(2,M+2):
    D[data[i]] = 0
B = data[-N:]
for i in range(N):
    if data[-(i+1)] in D:
        D[data[-(i+1)]]=1 
        count+=1
print(count)
for key in sorted(D.keys()):
    if D[key] ==1:
        print(key)