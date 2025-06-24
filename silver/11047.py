import sys
data = sys.stdin.read().split()
N,K = int(data[0]), int(data[1])
money = list(map(int, reversed(data[2:])))
count=0
idx = 0
amount = 0
while K>0:
    this_coin = K//money[idx]
    count+= this_coin
    
    this_amount = money[idx] * this_coin
    amount+= this_amount
    
    K -= this_amount
    idx+=1
print(count)