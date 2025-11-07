import sys
N = int(input())
if N<=5:
    print(N)
    sys.exit()

hex = set([1])
i=2
while True:
    num = 2*i*i-i
    if (num)>N:
        break
    if num==N:
        print(1)
        sys.exit()
    hex.add(num)
    
    i+=1

two = set([2])
for x in hex:
    for y in hex:
        if x+y==N:
            print(2)
            sys.exit()
        if x+y<N:
            two.add(x+y)

if N>146858:
    print(3)
    sys.exit()

three=set([3])
for x in hex:
    for y in two:
        if x+y==N:
            print(3)
            sys.exit()
        if x+y<N:
            three.add(x+y)

if N>130:
    print(4)
    sys.exit()

four = set([4])

for x in hex:
    for y in three:
        if x+y==N:
            print(4)
            sys.exit()
        if x+y<N:
            four.add(x+y)

for x in two:
    for y in two:
        if x+y==N:
            print(4)
            sys.exit()
        if x+y<N:
            four.add(x+y)


if N>26:
    print(5)
    sys.exit()

five = set([5])
for x in hex:
    for y in four:
        if x+y==N:
            print(5)
            sys.exit()
        if x+y<N:
            five.add(x+y)

for x in two:
    for y in three:
        if x+y==N:
            print(5)
            sys.exit()
        if x+y<N:
            five.add(x+y)

print(6)