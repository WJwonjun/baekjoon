#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int T,x1, y1, r1,x2,y2,r2;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        double distance = sqrt(pow((x2-x1),2)+pow((y2-y1),2));
        int minus = abs(r2-r1);   

        if (distance==0){
            if (r1==r2) printf("-1");
            else printf("0");
        }        

        else if (distance<minus) printf("0");
        else if (distance==minus) printf("1");
        else if (distance>minus && distance<(r2+r1)) printf("2");
        else if (distance==(r1+r2)) printf("1");
        else printf("0");
        printf("\n");
    }
    

}