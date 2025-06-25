
Com = int(input()) #<=100
M = int(input())
dic= {i+1:[] for i in range(Com)}

for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = set()
stack = [1]

while stack:
    current = stack.pop()
    if current not in visited:
        visited.add(current)
        for neighbor in dic[current]:
            if neighbor not in visited:
                stack.append(neighbor)

print(len(visited)-1)