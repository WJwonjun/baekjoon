def count_ones(n):
    if n<=0:
        return 0
    i=0
    while (1<<(i+1)) <= n:
        i+=1
    p = 1 << i
    return i*(p >> 1) + n-p+1 +count_ones(n-p)


A, B = map(int, input().split())
print(count_ones(B) - count_ones(A - 1))