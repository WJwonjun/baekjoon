m = input()
n = m.split('-')
answer = 0

x = sum(map(int,n[0].split('+')))
if m[0] =='-':
    answer-=x
else:
    answer+=x

for x in n[1:]:
    answer-=sum(map(int,x.split('+')))
    
print(answer)
