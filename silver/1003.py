import sys
data = sys.stdin.read()
T = int(data[0])
nums = list(map(int,data[1:].split()))
def fib(num,zero_count,one_count):
    if num==0:
        zero_count+=1
    elif num==1:
        one_count+=1
    else:
        zero_count, one_count = fib(num-1,zero_count,one_count)
        zero_count, one_count = fib(num-2,zero_count,one_count)
    return zero_count, one_count

for num in nums:
    z, o = fib(num,0,0)
    print(z,o)