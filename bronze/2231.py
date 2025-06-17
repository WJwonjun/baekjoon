num = int(input())
tmp = num
zero_num = 0
while tmp>0:
    tmp//=10
    zero_num+=1
start = max(0,num-9*zero_num)
for i in range(start,num):
    j=i
    total = i
    while j>0:
        total += j%10
        j//=10
    if total==num:
        print(i)
        break
else:
    print(0)