#include <stdio.h>
 

#define min(x,y) x<y ? x:y
int main(){
    int N,M;
    scanf("%d %d",&N,&M);
    char nums[N][M];
    for (int i=0;i<N;i++){
            scanf("%s",&nums[i]);
    }

    int l = min(N,M);
    int flag=0;
    while (l>0){
        for (int i=0;i+l<=N;i++){
            for (int j=0;j+l<=M;j++){
                //printf("%d %d %d %d %d\n",l,nums[i][j],nums[i+l-1][j],nums[i][j+l-1],nums[i+l-1][j+l-1] );
                if (nums[i][j]==nums[i+l-1][j] && nums[i][j+l-1]==nums[i+l-1][j+l-1] && nums[i][j]==nums[i][j+l-1]){
                    printf("%d",l*l);
                    flag=1;
                }
                if (flag==1) break;
            }
            if (flag==1) break;
        }
        if (flag==1) break;
        l--;
    }
}