N = int(input())
data_groups = [[] for _ in range(50)]
for i in range(N):
    word = input()
    l = len(word)-1
    if word in data_groups[l]:
        continue
    data_groups[l].append(word)
for i in range(50):
    if len(data_groups[i])==0:
        continue
    data_groups[i] = sorted(data_groups[i])
    for item in data_groups[i]:
        print(item)
    
