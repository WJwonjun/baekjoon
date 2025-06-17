num_list = []
for i in range(3):
    num_list.append(input())
    if num_list[i].isdigit():
        target_num = int(num_list[i])+3-i
if target_num%3==0:
    if target_num%5==0:
        print('FizzBuzz')
    else:
        print('Fizz')
else:
    if target_num%5==0:
        print('Buzz')
    else:
        print(target_num)