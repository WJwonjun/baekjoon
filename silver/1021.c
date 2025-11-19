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
    if (q->head == q->tail){
        q->head = NULL;
        q->tail = NULL;
    } else {
        q->head = q->head->right;
        q->head->left = NULL;
    }
    q->len--;
    free(delnode);
}

/*
 * 1-shot rotate
 * command == 'l' : 왼쪽으로 n칸 회전
 * command == 'r' : 오른쪽으로 n칸 회전
 */
void rotate(QUEUE* q, char command, int n){
    if (q->len <= 1) return;

    n %= q->len;            // 한 바퀴 이상 도는 건 줄여줌
    if (n == 0) return;

    // 오른쪽 회전은 "len - n"만큼 왼쪽 회전과 같음
    if (command == 'r'){
        n = q->len - n;
    }

    // 여기부터는 "왼쪽으로 n칸 회전"만 구현
    // 새 tail = head에서 n-1칸 이동한 노드
    NODE* new_tail = q->head;
    for (int i = 0; i < n - 1; i++){
        new_tail = new_tail->right;
    }
    NODE* new_head = new_tail->right;

    // 일단 원형으로 만들고
    q->tail->right = q->head;
    q->head->left = q->tail;

    // 새 head / tail 기준으로 끊기
    new_head->left = NULL;
    new_tail->right = NULL;

    q->head = new_head;
    q->tail = new_tail;
}

int find(QUEUE* q, int num){
    if (q->len <= 0) return 0;
    int cnt = 0;
    NODE* cur = q->head;
    while (cur){
        if (cur->item == num) return cnt;
        cur = cur->right;
        cnt++;
    }
    return -1;  // 이론상 오면 안 됨
}

int main(){
    int N, M;
    int num, place;
    int ans = 0;

    scanf("%d %d", &N, &M);
    QUEUE* q = init();

    // 1 ~ N 넣어야 백준 1021과 매칭됨
    for (int i = 1; i <= N; i++){
        append(q, i);
    }

    for (int j = 0; j < M; j++){
        scanf("%d", &num);
        place = find(q, num);        // 현재 num의 index (0-based)

        int left = place;            // 왼쪽으로 회전할 횟수
        int right = q->len - place;  // 오른쪽으로 회전할 횟수

        if (left <= right){
            rotate(q, 'l', left);
            ans += left;
        } else {
            rotate(q, 'r', right);
            ans += right;
        }

        pop(q); // 맨 앞 원소 제거
    }

    printf("%d", ans);
    return 0;
}
