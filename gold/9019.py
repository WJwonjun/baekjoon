import sys
from collections import deque,defaultdict


def bfs(start, target):
    visited = [False] * 10000
    queue = deque()
    queue.append((start, ""))
    visited[start] = True

    while queue:
        num, ops = queue.popleft()
        if num == target:
            return ops

        # D operation
        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, ops + 'D'))

        # S operation
        s = 9999 if num == 0 else num - 1
        if not visited[s]:
            visited[s] = True
            queue.append((s, ops + 'S'))

        # L operation
        l = int(str(num).zfill(4)[1:] + str(num).zfill(4)[0])
        if not visited[l]:
            visited[l] = True
            queue.append((l, ops + 'L'))

        # R operation
        r = int(str(num).zfill(4)[-1] + str(num).zfill(4)[:-1])
        if not visited[r]:
            visited[r] = True
            queue.append((r, ops + 'R'))

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    print(bfs(x, y))