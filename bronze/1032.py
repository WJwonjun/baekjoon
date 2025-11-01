import sys
input = sys.stdin.readline
N = int(input())

chars = []
for _ in range(N):
    chars.append(list(input().strip()))


for j in range(1,N):
    for k in range(len(chars[0])):
        if chars[0][k]=='?'or chars[0][k]== chars[j][k]:
            continue
        else:
            chars[0][k] = '?'


print(''.join(chars[0]))

