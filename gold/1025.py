import sys, math

input = sys.stdin.readline

N,M = map(int,input().split())

nums = [list(map(int,input().strip())) for _ in range(N)]
#print(nums)

def is_square(n):
    if n<0:
        return False
    root =  int(math.sqrt(n))
    return root*root==n

ans=-1
for i in range(1,max(N,M)+1):
    for start_n in range(0,N):
        for start_m in range(0,M):
            for dn in range(-start_n,N-start_n):
                for dm in range(-start_m,M-start_m):
                    cur = []
                    n = start_n
                    m = start_m

                    if dn==0 and dm==0:
                        if max(N,M)==1:
                            cur.append(nums[0][0])
                        else:
                            continue
                    else:
                            cnt=0
                            while 0<=n<N and 0<=m<M and cnt<i:
                                cur.append(nums[n][m])
                                cnt+=1
                                n+=dn
                                m+=dm 

                    now = int(''.join(map(str,cur)))
                    if is_square(now):
                        ans = max(ans,now)
                    #print(cur,dn,dm)                      

print(ans)


#우하하
