
import sys
from itertools import combinations
input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit

N,K = list(map(int, input().rstrip().split()))
essential = 532741
words = [list(input().rstrip()) for _ in range(N)]
bits = list(map(word2bit, words))

if K<5:
    print(0)
elif K>=26:
    print(N)

else:
    alphabet = [1 << i for i in range(26) if not (essential & 1 << i)] # 필수가 아닌 21개의 알파벳
    answer = 0  
    for comb in combinations(alphabet,K-5):
        know = sum(comb)|essential
        count = 0
        for bit in bits:
            if bit&know==bit:
                count+=1
        answer = max(answer,count)
    print(answer)