#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    int data;
    struct _node* prev;
} Node;

typedef struct _linkedList {
    Node* head;
    Node* tail;
    int len;
} LinkedList;

void initlist(LinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
    list->len = 0;
}

void append(LinkedList* list, int data) {
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->data = data;
    newnode->prev = NULL;

    if (list->head == NULL) {
        list->head = newnode;
        list->tail = newnode;
    } else {
        newnode->prev = list->tail;
        list->tail = newnode;
    }
    list->len++;
}

int pop(LinkedList* list) {
    if (list->tail == NULL) {
        return -1;
    }

    Node* lastnode = list->tail;
    int x = lastnode->data;

    list->len--;
    if (list->len == 0) {
        list->head = NULL;
        list->tail = NULL;
    } else {
        list->tail = lastnode->prev;
    }

    free(lastnode);
    return x;
}

int main() {
    int x;
    scanf("%d", &x);

    LinkedList* list = (LinkedList*)malloc(sizeof(LinkedList));
    initlist(list);

    int cnt = 1;
    int sum = 64;

    append(list, 64);

    while (sum > x) {
        int last = pop(list);   // take the last stick
        last /= 2;              // cut it in half

        if ((sum - last) >= x) {
            append(list, last);
            sum -= last;        // discard one half
        } else {
            append(list, last);
            append(list, last); // keep both halves
            cnt++;
        }
    }

    printf("%d\n", cnt);

    // cleanup
    while (list->len > 0) pop(list);
    free(list);

    return 0;
}
