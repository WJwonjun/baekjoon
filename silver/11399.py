N = int(input())
data= list(map(int,input().split()))
data.sort()
count=0
for i in range(N):
    count+= data[i]*(N-i)
print(count)