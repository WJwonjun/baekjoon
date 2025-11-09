r1,c1,r2,c2 = map(int,input().split())



"""
새로운 사각형이 시작되는 위치 (0,0), (0,1), (1,2), (2,3)
ex. -1, -1
행과 열 중 max값 -> 1(그럼 2와 9 사이겠다)
두번째 사각형의 시작위치는 0,1
그럼 -1-1부터 0,1까지는 얼마나 차이가 나지?

여기서부턴 복잡하게 계산할 것 없이, 어차피 윈도우의 크기가 작으니까 노가다 가능하지 않을까
"""
nums = []

for r in range(r1,r2+1):
    tmp = []
    for c in range(c1,c2+1):
        if r==0 and c==0:
            tmp.append(1)
        else:
            box = max(abs(r),abs(c))
            start = (box*2-1)**2
            l = (box*2+1)**2-(box*2-1)**2

            if c==box and r<box:        # 오른쪽 I
                tmp.append(start+(box-r))

            elif r==box*(-1) and c<box: # 위쪽 ㅡ
                tmp.append(start+int(l/4)+(box-c))

            elif c==box*(-1) and r> box*(-1):
                tmp.append(start+int(l/4)*2+(r-box*(-1)))

            elif r==box and c>box*(-1):
                tmp.append(start+int(l/4)*3+(c-box*(-1)))
            


    nums.append(tmp)


max_len =0
for i in range(r2-r1+1):
    for n in nums[i]:
        max_len = max(max_len,len(str(n)))

for i in range(r2-r1+1):
    for n in nums[i]:
        print(" " * (max_len-len(str(n))),str(n),sep="",end=" ")
    print("")
