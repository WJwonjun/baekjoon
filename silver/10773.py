N = int(input())
stack=[]
for i in range(N):
    num = int(input())
    if num!=0:
        stack.append(num)
    if num==0:
        stack.pop()

print(sum(stack))