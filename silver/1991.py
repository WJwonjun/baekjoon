import sys
from collections import defaultdict,deque
input = sys.stdin.readline



N = int(input())
nodes = defaultdict()

for i in range(N):
    parent,left,right = input().split()
    nodes[parent]=[left,right]

def first(nodes):
    stack = ['A']
    ans_1 = []
    while stack:
        target = stack.pop()
        ans_1.append(target)
        
        if nodes[target][1]!='.':
            stack.append(nodes[target][1])
        if nodes[target][0]!='.':
            stack.append(nodes[target][0])
    return ''.join(ans_1)
print(first(nodes))


def inorder_iterative(nodes):
    stack = []
    curr = 'A'
    ans = []

    while stack or curr != '.':
        while curr != '.':
            stack.append(curr)
            curr = nodes[curr][0]
        curr = stack.pop()
        ans.append(curr)
        curr = nodes[curr][1]
    return ''.join(ans)
print(inorder_iterative(nodes))

def postorder_iterative(nodes):
    stack1 = ['A']
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        if node == '.':
            continue
        stack2.append(node)
        # 왼 → 오 → 루트를 뒤집기 위해: 루트 → 오 → 왼 push
        stack1.append(nodes[node][0])
        stack1.append(nodes[node][1])

    return ''.join(stack2[::-1])

print(postorder_iterative(nodes))