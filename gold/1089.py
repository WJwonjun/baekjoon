import sys
from itertools import product
input = sys.stdin.readline
N = int(input())
def sharp2bit(char):
    if char=="#":
        return 1
    elif char=='.':
        return 0
    
maps = [list(map(sharp2bit,input().strip())) for _ in range(5)]

def decode(num):
    codes = [0b111101101101111,0b001001001001001,0b111001111100111,0b111001111001111,0b101101111001001,0b111100111001111,0b111100111101111,0b111001001001001,0b111101111101111,0b111101111001111]
    ans = []
    for i in range(10):
        if num&codes[i] ==num:
            ans.append(i)
            #print(i)
    if not ans:
        print(-1)
        sys.exit(0)
    return ans

sum=[]
for i in range(N):
    num = []
    for j in range(5):
        num += maps[j][4*i:4*i+3]
    num = ''.join(map(str,num))
    sum.append(decode(int(num,2)))
length = []

for i in range(N):
    length.append(len(sum[i]))

# print(sum)
# print(length)
cnt = 1
for i in range(N):
    cnt*=length[i]
for i in range(N):
    length[i]=(cnt//length[i])
#print(length)

ans=0
for i in range(N):
    for c in sum[i]:
        ans += c*(10**(N-i-1))*length[i]
print(ans/cnt)