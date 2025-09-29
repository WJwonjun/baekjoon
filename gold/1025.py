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

for start_n in range(0,N):
    for start_m in range(0,M):
        for dn in range(-start_n,N-start_n):
            for dm in range(-start_m,M-start_m):
                cur = []
                n = start_n
                m = start_m

                if dn==0 and dm==0:
                    if max(N,M)==1:
                        now = nums[0][0]
                        if is_square(nums[0][0]):
                            ans =max(ans,now)
                    else:
                        continue

                else:
                        while 0<=n<N and 0<=m<M:
                            cur.append(nums[n][m])
                            n+=dn
                            m+=dm 

                            now = int(''.join(map(str,cur)))
                            if is_square(now):
                                ans = max(ans,now)
                #print(cur,dn,dm)                      

print(ans)


#우하하
