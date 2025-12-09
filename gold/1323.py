import sys
input = sys.stdin.readline
N,K = map(int,input().split())
l = len(str(N))
tmp = N

cnt = 0
while cnt<K:
    if cnt!=0:
        tmp = tmp*(10**(l)) + N
    tmp = tmp%K

    #print(cnt,tmp)

    if tmp==0: 
        print(cnt+1)
        break
    cnt+=1

else:
    print(-1)