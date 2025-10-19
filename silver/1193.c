#include <stdio.h>

int main(){
    int N;
    scanf("%d",&N);

    int tmp=1;
    while(1){
        if(N-tmp>0){
            N -=tmp;
            tmp+=1;
        }
        
        else break;
    }
    tmp+=1;
    if (tmp%2==1){
        printf("%d/%d",N,tmp-N);
    }
    else{
        printf("%d/%d",tmp-N,N);
    }
}