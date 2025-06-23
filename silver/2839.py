N = int(input())
ans = 0
chk=0
M = N//5

for i in range(M,-1,-1):
    ans=0
    share, remainder = 5*i, N-5*i
    ans+=i
    if remainder%3==0:
        ans+=remainder//3
        chk=1
        break
    
if chk==1:
    print(ans)
else:
    print(-1)
