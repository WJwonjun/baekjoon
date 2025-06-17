def func(k,n):
    if k==0:
        return n
    elif k==1:
        for i in range(n):
            sum += (i+1)
    else:
        for i in range(n):
            sum += i * func(k-2, n-i+1)
    return sum
    
N = int(input())
for i in range(N):
    k = int(input())
    n = int(input())
    print(func(k,n))
    
        