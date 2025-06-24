import sys
input = sys.stdin.readline

N, M = map(int, input().split())
enc = {}
dec = {}

for i in range(1, N + 1):
    name = input().strip()
    enc[str(i)] = name   # 번호로 이름 검색
    dec[name] = str(i)   # 이름으로 번호 검색

for _ in range(M):
    q = input().strip()
    if q in enc:
        print(enc[q])
    else:
        print(dec[q])