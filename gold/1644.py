
N = int(input())
if N==1:
    print(0)
else:
    sosu = [True]*(N+1)
    sosu[1] = False
    sosu[0] = False


    for i in range(1,N+1):
        if sosu[i] ==True:
            for j in range(2,N//i+1):
                sosu[i*j]=False
    #소수 찾기(NlogN)
    sosu_list = []
    for i in range(2,N+1):
        if sosu[i] ==True:
            sosu_list.append(i)
    # 소수 리스트 만들기 (N)

    left = 0
    right = 0
    count = 0
    cur = sosu_list[0]
    L = len(sosu_list)





    while left<=right :
        if cur<N:
            right+=1
            if right==L:
                break
            cur+=sosu_list[right]


        elif cur==N:
            count+=1
            right+=1
            if right==L:
                break
            cur+=sosu_list[right]


        else:
            cur-=sosu_list[left]
            left+=1
            if left==L:
                break

    # two pointer (logN~N?)

    print(count)

    #메모리 2*N