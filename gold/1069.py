import math
X,Y,D,T = map(int,input().split())

length = math.sqrt(X**2+Y**2)
def spf(length,cnt):
    #print(length,cnt)

    if 0<length<D:
        return min(cnt+length,cnt+T+(D-length),cnt+2*T) # 그냥 걸어가기, 음수 영역 점프 후 걷기, 두번 점프
    elif length==D:
        return cnt+min(T,length) #점프 혹은 걷기
    elif D<length<=2*D:
        return min(spf(length-D,cnt+T),cnt+2*T,cnt+length) # 한번 점프, 두번 점프, 그냥 걷기(점프 효율 떨어짐) 
    elif length>2*D: # 한번 점프, 2D까지만 걸어가기
        return min(spf(length-D,cnt+T),spf(2*D,cnt+(length-2*D)))

print(float(spf(length,0)))    