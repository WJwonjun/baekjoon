import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
peoples = [i for i in range(1,N+1)]

enemy = deque(map(int,input().split()))
enemy.popleft()

count=0

parties = [list(map(int,input().split()))[1:] for _ in range(M)]

while enemy:
    target = enemy.popleft()
    for i in range(len(parties)):
        if target in parties[i]:
            for guest in parties[i]:
                if guest!=target:
                    enemy.append(guest)
            parties[i] = []  
            
for party in parties:
    if len(party)>0:
        count+=1
print(count)
    
    