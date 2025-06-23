T = int(input())
check = 0
for i in range(T):
    sentence = input()
    check=0
    for word in sentence:
        if word == '(':
            check+=1
        elif word ==')':
            check-=1
            if check<0:
                break
    if check==0:
        print('YES')
    else:
        print('NO')
                
            
                