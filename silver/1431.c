#include <stdio.h>
#include <string.h>

int compare(char* a, char* b){
    if(strlen(a)<strlen(b)) return -1;
    else if (strlen(a)>strlen(b)) return 1;

    else{
        int num_a=0,num_b=0;
        for(int i=0;i<strlen(a);i++){
            if('0' <= a[i] && a[i] <= '9') num_a+=a[i]-'0';
        }
        for(int i=0;i<strlen(b);i++){
            if('0' <= b[i] && b[i] <= '9') num_b+=b[i]-'0';
        }

        if(num_a<num_b) return -1;
        else if (num_a>num_b) return 1;
        else{
            return strcmp(a,b);
        } 
    }
}

void swap(char *a, char *b){
    char tmp[51];
    strcpy(tmp,a);
    strcpy(a,b);
    strcpy(b,tmp);
}

int main(){
    int N;
    scanf("%d",&N);
    char serial[N][51];
    for(int i=0;i<N;i++){
        scanf("%s",serial[i]);
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N-i-1;j++){
            if(compare(serial[j],serial[j+1])>0) swap(serial[j],serial[j+1]);
        }
    }
    for (int i=0;i<N;i++){
        printf("%s\n",serial[i]);
    }
}