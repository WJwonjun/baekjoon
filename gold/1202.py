import sys,heapq
input = sys.stdin.readline
N,K = map(int,input().split())

jews=[]
for _ in range(N):
    M,V = map(int,input().split())
    heapq.heappush(jews,(M,V))
# (무게, 가격) 오름차순

cap = []
for _ in range(K):
    C = int(input())
    cap.append(C)
cap.sort()
# 작은 가방부터

waste = []
#쓰레기통

ans =0

for i in range(K):
    if waste:
        tmp_v = (-1)*heapq.heappop(waste)
    else:
        tmp_v = 0
    # 쓰레기통에 남아있는 가장 비싼 보석 기준 시작
    # 전 가방보다 가벼웠으므로 무게는 검사할 필요 없음

    while jews:
        m,v = heapq.heappop(jews)
        if m>cap[i]:
            heapq.heappush(jews,(m,v))
            break
        ## 무겁네 ㅎㅎㅈㅅ

        elif v>=tmp_v:
            if tmp_v!=0:
                heapq.heappush(waste,(-tmp_v))
            tmp_v = v
        ## 가능한 제일 무거운 값 찾음

        else:
            if tmp_v!=0:
                heapq.heappush(waste,(-v))
        ## 무시할 만한 애들은 다시 놓고 다음거 찾음

    #print(i,jews, waste,tmp_v)        

        # tmp_v가 1등상, 아무것도 안되면 waste 라도 넣어야
        # 쓰레기통은 가치 큰 순 정렬해야 함
    ans+=tmp_v

print(ans)