import sys
input = sys.stdin.read

data = list(map(int, input().split()))
N = data[0]
students = []
for i in range(N):
    w, h = data[2*i+1],data[2*i+2]
    students.append((w,h))
for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank, end=' ')