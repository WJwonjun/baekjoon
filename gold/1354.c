#include <stdio.h>
#include <stdlib.h>



typedef struct node{
    long long key, value;
    struct node* next;
}NODE;

NODE* hash[100003];

long long cal(long long N, long long P, long long Q, long long X, long long Y){
    if(N<=0) return 1;
    else if(find(N)!=0){
        return find(N);
    }
    else{
        insert(N,cal(N/P-X)+cal(N/Q-Y));
        return cal(N/P-X)+cal(N/Q-Y);
    }
}

long long find(long long N){
    long long curkey = N%100003;
    NODE* p = hash[h];
    while(p){
        if(p->key == curkey) return p->value;
        else p = p->next;
    }
    return 0;
}

void insert(long long N, long long val){
    long long curkey = N%100003;
    NODE* newnode = malloc(sizeof(NODE));
    newnode->key = curkey;
    newnode->value = val;
    newnode->next = hash[curkey];
    hash[curkey] = newnode;
}


int main(){
    long long N,P,Q,X,Y;
    scanf("%lld %lld %lld %lld %lld",&N,&P,&Q,&X,&Y);
    printf("%lld",cal(N,P,Q,X,Y));
}