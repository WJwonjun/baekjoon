N =int(input())
arr =[]
for i in range(N):
    age, name = input().split()
    arr.append((int(age), i, name))
arr.sort(key = lambda x: (x[0],x[1]))

for id in arr:
    print(id[0],id[2])