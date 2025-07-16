import sys
sys.setrecursionlimit(10 ** 4+10)

nums = []
while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        nums.append(int(line))
    except:
        break

output = []

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if nums[i] > nums[start]:
            mid = i
            break
    post(start + 1, mid - 1)
    post(mid, end)
    output.append(str(nums[start]))

post(0, len(nums) - 1)

sys.stdout.write('\n'.join(output) + '\n')