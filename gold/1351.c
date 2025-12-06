#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    long long key, value;
    struct Node *next;
}NODE;

NODE *hash[100003];

long long find(long long x){
    long long h = x % 100003;
    NODE *p = hash[h];
    while(p){
        if(p->key == x) return p->value;
        p = p->next;
    }
    return -1;
}

void insert(long long x, long long y){
    long long h = x%100003;
    NODE *node = malloc(sizeof(NODE));
    node->key = x;
    node->value = y;
    node->next = hash[h];
    hash[h] = node;
}

long long cal(long long N,long long P, long long Q){
    if(N==0) return 1;
    long long val = find(N);
    if(val!=-1) return val;

    long long result = cal(N/P,P,Q)+cal(N/Q,P,Q);
    insert(N,result);
    return result;
}

int main(){
    long long N,P,Q;
    scanf("%lld %lld %lld",&N,&P,&Q);
    printf("%lld",cal(N,P,Q));
}