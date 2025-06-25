import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid for tree in trees if tree > mid)
    
    if total >= M:
        result = mid  
        start = mid + 1
    else:
        end = mid - 1

print(result)