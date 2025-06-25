from collections import defaultdict
import sys
N = int(input())
for _ in range(N):
    M = int(input())
    dic=defaultdict(list)
    for i in range(M):
        word = list(sys.stdin.readline().split())
        dic[word[1]].append(word[0])
    result=1
    for key in dic:
        result*= (len(dic[key])+1)
    print(result-1)