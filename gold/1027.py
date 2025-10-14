import sys
input = sys.stdin.readline
N= int(input())
nums = list(map(int,input().split()))
ans=0
for i in range(N):
    l_slope = int(1e9)
    r_slope = -int(1e9)
    cnt=0
    for l in range(i-1,-1,-1):
        x_slope = (nums[i]-nums[l])/(i-l)
        if x_slope<l_slope:
            cnt+=1
            l_slope = x_slope
    for r in range(i+1,N):
        x_slope = (nums[r]-nums[i])/(r-i)
        if x_slope>r_slope:
            cnt+=1
            r_slope = x_slope

    ans = max(cnt,ans)
print(ans)