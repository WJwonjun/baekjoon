#include <stdio.h>

int main(){
    int N, S, ans=0;
    scanf("%d %d",&N,&S);
    int nums[N];
    for(int i=0;i<N;i++){
        scanf("%d",&nums[i]);
        //printf("%d ",nums[i]);
    }
    for(int i = 1; i < (1 << N); i++){ // 전체 경우의 수 (1~2^N-1)
        int tmp = 0;
        for (int j = 0; j < N; j++) {   // 자릿수
        if(((i >> j) & 1)==1) tmp+= nums[j];
    }
        if (tmp==S) ans++;
    }
    printf("%d",ans);

}