L = int(input())
chars = list(input())
chars = [ord(c)-ord('a')+1 for c in chars]
result = 0

for i in range(L):
    result += chars[i]*(31**i)
print(result%1234567891)