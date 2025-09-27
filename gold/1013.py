import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    nums = list(map(int,input().strip()))
    #print(nums)

    zero_cnt = 0
    one_cnt = 0

    while nums:
        cur = nums.pop()

        if cur==0:
            if len(nums)==0:
                if one_cnt==1 and zero_cnt==0:
                    print("YES")
                    break
                else:
                    print("NO")
                    break

            else:
                    zero_cnt+=1



        elif cur==1:
            if zero_cnt==0:
                if len(nums)==0:
                    print("NO")
                    break

                one_cnt+=1

            elif zero_cnt==1:
                if one_cnt==1:
                    if len(nums)==0:
                        print("NO")
                        break
                    zero_cnt,one_cnt = 0,1
                else:
                    print("NO")
                    break

            elif zero_cnt>=2:
                if one_cnt>=1:
                    zero_cnt,one_cnt=0,0
                else:
                    print("NO")
                    break
        #print(cur,nums,zero_cnt,one_cnt)

    else: 
        print("YES")

#우하하하