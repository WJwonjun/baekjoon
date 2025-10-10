import sys

N = int(sys.stdin.readline())
# 최대 9876543210 -> 이게 2^10-1 = 1023번째
if N>1023:
    print(-1)
    sys.exit(0)

nums = []

# 10비트 정수 만들기
weights = list(range(9,-1,-1))

for n in range(0b0000000001,0b1111111111+1):
    result = ""

    for i,w in enumerate(weights):
        bit = ((n>>(9-i))&1)
        if bit!=0:
            bit*=w
            result +=str(bit)

    nums.append(int(result))
    
nums.sort()
print(nums[N-1])