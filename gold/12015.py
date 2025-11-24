import sys
import bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

ans = []


for num in nums:
    pos = bisect.bisect_left(ans,num)
    if pos==len(ans):
        ans.append(num)
    else:
        ans[pos] = num
    print(ans)
print(len(ans))


# ans: 실제 LIS 리스트가 아니라, 후에 나오는 숫자가 ans[i]보다 크고 ans[i+1]보다 작으면 그 수는 i값을 가지게 될 것.