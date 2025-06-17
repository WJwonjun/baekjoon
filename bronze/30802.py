total_nums = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())

total_T = 0 
for size in size_list:
    tmp = (size-1)//T + 1
    total_T +=tmp
print(total_T)
print(total_nums//P, total_nums%P)