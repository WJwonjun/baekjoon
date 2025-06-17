digits = list(input())
check = (10 - int(digits[-1]))%10

result = 0
three=0
for i in range(len(digits)-1):
    if i%2==1: # 실제론 짝수
        if digits[i]=='*':
            three=1
        else:
            result+=3*int(digits[i])
    else:
        if digits[i]=='*':
            continue
        else:
            result+= int(digits[i])

if three==1:
    for i in range(10):
        if (result + i*3)%10 == check:
            print(i)
            break
else:
    for i in range(10):
        if (result + i)%10 == check:
            print(i)
            break
            