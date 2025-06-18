import sys

arr = [0]*1000000

input = sys.stdin.read
data = list(map(int, input().split()))
N = data[0]
numbers = data[1:]

# 입력 처리
for num in numbers:
    arr[num - 1] += 1

for i in range(1000000):
    if arr[i]==1:
        print(i+1)