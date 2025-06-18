N = int(input())
five = 0
for i in range(1,N+1):
    num=i
    if num%5==0:
        while num%5==0:
            num//=5 
            five+=1

print(five)