import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int,input().split()))
M = max(cards)
x = set(cards)
che = [0]*(M+1)

for card in cards:
    if card==M:
        continue
    for i in range(2*card,M+1,card):
        if i in x:
            che[card]+=1
            che[i]-=1
for card in cards:
    print(che[card],end=" ")