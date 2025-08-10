import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

L = [1]*N
for i in range(N):
    for j in range(i):
        if nums[j]<nums[i]:
            L[i]=max(L[i],L[j]+1)

R = [1]*N
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if nums[j]<nums[i]:
            R[i] = max(R[i],R[j]+1)

print(max(L[i]+R[i]-1 for i in range(N)))