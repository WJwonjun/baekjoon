import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-bomb_len:])==bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

    