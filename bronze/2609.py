N, M = map(int,input().split())
big_num = N*M

for i in range(min(N,M),0,-1):
    if N%i==0 and M%i==0:
        print(i)
        print(big_num//i)
        break