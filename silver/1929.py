M, N = map(int, input().split())
for i in range(M, N+1):
    if i==1:
        continue
    chk=0
    for j in range(2,int(i**0.5) +1):
        if i%j==0:
            chk=1
            break
    if chk==0:
        print(i)