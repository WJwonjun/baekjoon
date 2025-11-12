#include <stdio.h>
#include <math.h>

double distance(int x1,int y1,int x2, int y2){

    return sqrt(pow((x2-x1),2)+pow((y1-y2),2));
}

int main(){
    int T,x1,y1,x2,y2,n;
    int cnt,cx,cy,r;

    scanf("%d",&T);
    for(int i=0;i<T;i++){
        scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
        scanf("%d",&n);
        cnt=0;

        for(int j=0;j<n;j++){
            scanf("%d %d %d",&cx, &cy,&r);
            if (distance(x1,y1,cx,cy)<r && distance(x2,y2,cx,cy)<r) continue;
            else if (distance(x2,y2,cx,cy)<r) cnt++;
            else if (distance(x1,y1,cx,cy)<r) cnt++;
        }
        printf("%d\n",cnt);
    }
}