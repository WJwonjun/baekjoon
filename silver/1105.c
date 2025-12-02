#include <stdio.h>
#include <string.h>

int main(){
    char L[11],R[11];
    scanf("%s %s",L,R);
    if (strlen(L)!=strlen(R))printf("0");
    else{
        int cnt=0;
        for(int i=0;i<strlen(L);i++){
            if(L[i]=='8' && R[i]=='8')cnt++;
            else if (L[i]==R[i]) continue;
            else break;
        }
        printf("%d",cnt);
    }
}