while True:
    n = (input())
    if n=='0':
        break
    
    idx = 0
    k = len(n)
    
    for i in range(k//2):
        if n[i]==n[k-1-i]:
            continue
        else:
            idx = 1
            print('no')
            break
    if idx ==0:
        print('yes')