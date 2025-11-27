#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int item;
    struct node* prev;
    struct node* next;
} Node;

typedef struct list{
    int len;
    Node* head;
    Node* tail;
}List;

List* init(){
    List* list = malloc(sizeof(List));
    list->len = 0;
    list->head = NULL;
    list->tail = NULL;
    return list;
}

void append(List* list, int pos, int item){
    Node* node = malloc(sizeof(Node));
    node->item = item;
    if(list->len==0){    
        node->prev = NULL;
        node->next = NULL;
        list->head = node;
        list->tail = node;
        list->len++;
    }
    else{
        if(pos==0){
            node->prev = NULL;
            node->next = list->head;
            list->head->prev = node;
            list->head = node;

        }
        else if(pos==list->len){
            node->next = NULL;
            node->prev = list->tail;
            list->tail->next = node;
            list->tail = node;

        }
        else{
            Node* target = list->head;
            for(int k=0;k<pos-1;k++){
                target = target->next;
            }
                node->prev = target;
                node->next = target->next;
                target->next = node;
                node->next->prev = node;
        }
        list->len++;
    }
}


void traverse(List* list) {
    Node* curnode = list->head;
    while (curnode != NULL) {
        printf("%d ", curnode->item);
        curnode = curnode->next;
    }
}

int main(){
    int N;
    scanf("%d",&N);
    int data[N];
    
    List* list = init();
    for(int i=0;i<N;i++){
        scanf("%d",&data[i]);

    }
    for(int j=N-1;j>=0;j--){
        append(list,data[j],j+1);
        // traverse(list);
        // printf("\n");
    }

    traverse(list);


}