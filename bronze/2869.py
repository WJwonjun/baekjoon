A, B, V = map(int,input().split())
l , count= 0,  0
V -=B
count = V//(A-B) 
if V%(A-B)!=0:
    count+=1
print(count)
    