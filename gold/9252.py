import sys
input = sys.stdin.readline
a = list(input().strip())
b = list(input().strip())



dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]


for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

print(dp[len(a)][len(b)])

stack = []
while i>=0 and j>=0:
    if dp[i+1][j] > dp[i][j+1]:
        j-=1
    elif dp[i+1][j] < dp[i][j+1]:
        i-=1
    else:
        if dp[i][j]==dp[i+1][j+1]:
            i-=1
            j-=1
        else:
            if dp[i+1][j]==dp[i+1][j+1]:
                i-=1
            else:
                stack.append(a[i])
                i-=1
                j-=1

stack.reverse()
if dp[len(a)][len(b)]!=0:
    print(''.join(stack))