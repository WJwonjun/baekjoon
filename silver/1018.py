N, M = map(int, input().split())
arr = []
for i in range(N):
    
    arr.append(list(input()))

ans = 64
chk=0
for i in range(N-8 +1):
    for j in range(M-8+1):
        chk=0
        for k in range(8):
            for l in range(8):
                if arr[k+i][l+j]=='B' and (k+l)%2==0:
                        chk+=1
                elif arr[k+i][l+j]=='W' and (k+l)%2==1:
                        chk+=1
           
        ans = min(ans, chk,64-chk)
        
print(ans)