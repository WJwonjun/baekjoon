import sys
input = sys.stdin.readline

N = int(input())
Y = list(map(int,input().split()))


if N==1:
    print('A')
elif N==2 :
    if Y[0]==Y[1]:
        print(Y[0])
    else : print('A')
else:
    K = []
    for i in range(N-1):
        K.append(Y[i+1]-Y[i])
    
    if K[0]==0:
        for i in range(1,N):
            if Y[0]!=Y[i]:
                print('B')
                sys.exit(0)  
        print(Y[0])

    else:

        for slope in range(K[1]//K[0], K[1]//K[0]+2):  
            find = 1      
            for i in range(len(K)-1):
                if K[i]*slope!=K[i+1]:
                    find = 0

            if find==1:
                b = Y[1]-Y[0]*slope
                break

        else:
            print('B')
            sys.exit(0)

        for i in range(N-1):
            if Y[i]*slope+b!=Y[i+1]:
                print('B')
                sys.exit(0)
        
        print(Y[-1]*slope+b)
