#include <stdio.h>
#include <math.h>

#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y, z) \
    ((x) < (y) ? ((x) < (z) ? (x) : (z)) \
               : ((y) < (z) ? (y) : (z)))
int main(){
    int N,L,W,H;
    scanf("%d %d %d %d",&N,&L,&W,&H);

    
    double low = 0.0;
    double high = (double)(L < W ? (L < H ? L : H) : (W < H ? W : H));

    for (int i=0;i<100;i++){
        double cur = (low+high)/2.0;
        long long cnt = (long long)(L / cur) * (long long)(W / cur) * (long long)(H / cur);
        
        if (cnt>=N){
            low = cur;
        }
        else
            high = cur;
    }
    printf("%.9f",low);
}