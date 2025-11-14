#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    struct node* left;
    int item;
    struct node* right;
} NODE;

typedef struct queue{
    NODE* head;
    NODE* tail;
    int len;
} QUEUE;

QUEUE* init(){
    QUEUE* q = malloc(sizeof(QUEUE));
    q->head = NULL;
    q->tail = NULL;
    q->len = 0;
    return q;
}

void append(QUEUE* q, int n){
    NODE* node = malloc(sizeof(NODE));
    node->left = NULL;
    node->item = n;
    node->right = NULL;

    if(q->len == 0){
        q->head = node;
        q->tail = node;
    } else {
        q->tail->right = node;
        node->left = q->tail;
        q->tail = node;
    }
    q->len++;
}

void pop(QUEUE* q){
    NODE* delnode = q->head;

    if(q->head == q->tail){
        q->head = NULL;
        q->tail = NULL;
    } else{
        q->head = q->head->right;
        q->head->left = NULL;
    }

    q->len--;
    free(delnode);
}

void rotate(QUEUE* q, char command, int n){
    if(n <= 0) return;

    if(command == 'l'){
        for(int i = 0; i < n; i++){
            NODE* head = q->head;
            q->head = q->head->right;
            if(q->head) q->head->left = NULL;
            q->tail->right = head;
            head->left = q->tail;
            head->right = NULL;
            q->tail = head;
        }
    }
    else{
        for(int i = 0; i < n; i++){
            NODE* tail = q->tail;
            q->tail = q->tail->left;
            if(q->tail) q->tail->right = NULL;
            q->head->left = tail;
            tail->right = q->head;
            tail->left = NULL;
            q->head = tail;
        }
    }
}

int find(QUEUE* q, int num){
    NODE* cur = q->head;
    int cnt = 0;

    while(cur){
        if(cur->item == num) return cnt;
        cur = cur->right;
        cnt++;
    }
    return -1;
}

void print_queue(QUEUE* q) {
    NODE* cur = q->head;
    printf("Queue: ");
    while(cur) {
        printf("%d ", cur->item);
        cur = cur->right;
    }
    printf("(len=%d)\n", q->len);
}

int main(){
    int N, M;
    int num, place;
    int ans = 0;

    scanf("%d %d", &N, &M);
    QUEUE* q = init();

    for(int i=1; i<=N; i++){
        append(q, i);
    }

    printf("Initial: ");
    print_queue(q);

    for(int j=0; j<M; j++){
        scanf("%d", &num);
        place = find(q, num);

        int left = place;
        int right = q->len - place;

        printf("Looking for %d at position %d (left=%d, right=%d)\n", num, place, left, right);

        if(left <= right){
            rotate(q, 'l', left);
            ans += left;
        } else {
            rotate(q, 'r', right);
            ans += right;
        }

        printf("After rotate: ");
        print_queue(q);

        pop(q);
        printf("After pop: ");
        print_queue(q);
    }

    printf("%d", ans);
}
