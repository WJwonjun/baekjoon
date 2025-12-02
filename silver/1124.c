#include <stdio.h>


int get_prime(int N){
    int cnt=0;
    int tmp = N;
    for(int i=2;i<=N;i++){
        if(N%i==0){
            while(N%i==0){
                N/=i;
                cnt++;
            }
        }
        if (N==1) break;
    }
    //printf("%d %d\n",tmp, cnt);
    return cnt;
}


int main(){
    int A,B,cnt=0;
    scanf("%d %d",&A,&B);
    for(int N=A;N<=B;N++){
        int prime = get_prime(N);
        if(get_prime(prime)==1) cnt++;
    }
    printf("%d",cnt);
}