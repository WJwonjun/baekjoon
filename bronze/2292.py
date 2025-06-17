'''
시작 : 1
2 : 2~7 6
3 : 8~19 12
4 : 20~37 18
'''
n = int(input())-1
tmp=1
ans=1
while n>0:
    n -= 6*tmp
    ans += 1 
    tmp += 1
print(ans)
