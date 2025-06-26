import sys
input = sys.stdin.readline
K,N = map(int,input().split())

ropes = []
for i in range(K):
    ropes.append(int(input()))

start = 1
end = max(ropes)
result = 0

while start<= end:
    mid = (start+end)//2
    total = sum(rope//mid for rope in ropes)
    
    if total>= N:
        result = mid
        start = mid+1
    
    else:
        end = mid-1
print(result)