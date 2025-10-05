import sys
from collections import defaultdict,Counter
input = sys.stdin.readline
words = defaultdict(Counter)
while True:
    word = input().strip()
    if word=='-':
        break

    words[word] = Counter(word)
#print(words)

while True:
    chars=list(input().strip())
    if "#" in chars:
        break

    chars = Counter(chars)
    possible = []
    for word in words.keys():

        for word_ch in words[word].keys():
            #print(word_ch,words[word][word_ch])
            if not (word_ch in chars and words[word][word_ch]<=chars[word_ch]):
                break
        else:
            possible.append(word)
    #print(possible)
    ans = {i:0 for i in chars}
    for word in possible:
        chars = set(list(word))
        for char in chars:
            ans[char]+=1
    min_val, max_val = min(ans.values()),max(ans.values())
    min_list = sorted([k for k,v in ans.items() if v==min_val])
    max_list = sorted([k for k,v in ans.items() if v==max_val])
    print(''.join(min_list),min_val,end=" ")
    print(''.join(max_list),max_val)
                    

    

    

