#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#define GETCHAR getchar
#else
#define GETCHAR getchar_unlocked
#endif

static inline int read_int(void){
    int x = 0, c = GETCHAR(), neg=0;
    while(c<=' ') c = GETCHAR();
    if (c=='-') {neg=1; c = GETCHAR();}
    for (; c>='0'; c=GETCHAR())x=x*10+(c-'0');
    return neg ? -x : x;
}

typedef struct {int v; int w;} HNode;

typedef struct {
    HNode *a;
    int size;
    int cap;
}MinHeap;

static inline void heap_swap(HNode *x,HNode *y){HNode t=*x;*x=*y;*y=t;}

void heap_init(MinHeap *h, int cap){
    h -> a = (HNode*)malloc(sizeof(HNode)*(cap+1));
    h -> size = 0;
    h -> cap = cap;
}


void heap_push(MinHeap *h, int w, int v){
    int i = ++h->size;
    h->a[i].w = w; h->a[i].v=v;
    while (i>1){
        int p=i >>1;
        if (h->a[p].w <= h->a[i].w) break;
        heap_swap(&h->a[p],&h->a[i]);
        i=p;
    }
}

HNode heap_pop(MinHeap *h){
    HNode top = h->a[1];
    HNode last = h->a[h->size--];
    int i=1,l,r,m;
    while ((l=i<<1) <= h->size){
        r = l+1; m=l;
        if (r <= h->size && h->a[r].w < h->a[l].w) m=r;
        if (h->a[m].w >= last.w) break;
        h->a[i] = h->a[m]; i=m;
    }
    h->a[i] = last;
    return top;
}

int main(void){
    int N = read_int();
    int M = read_int();

    int *head = (int*)malloc(sizeof(int)*(N+1));
    for (int i=1;i<=N;++i) head[i]=-1;

    int E = M*2;
    int *to = (int*)malloc(sizeof(int)*(E));
    int *w = (int*)malloc(sizeof(int)*(E));
    int *next = (int*)malloc(sizeof(int)*(E));
    int ei = 0;

    for (int i=0; i<M; ++i){
        int u = read_int();
        int v = read_int();
        int c = read_int();

        to[ei]=v;w[ei]=c;next[ei]=head[u];head[u]=ei++;
        to[ei]=u;w[ei]=c;next[ei]=head[v];head[v]=ei++;
    }

    int *visited = (int*)malloc(sizeof(int)*(N+1));
    for (int i=1; i<=N; ++i) visited[i]= -1;

    MinHeap h; heap_init(&h,(M > 0 ? 2*M : 2));

    heap_push(&h,0,1);

    int taken = 0;
    long long sum = 0;
    int mx = 0;

    while (h.size && taken <N ){
        HNode cur = heap_pop(&h);
        int v = cur.v, cost = cur.w;

        if (visited[v]!=-1) continue;

        visited[v] = cost;
        ++taken;
        sum+=cost;
        if (cost > mx) mx=cost;

        for (int e = head[v];e!=-1;e=next[e]){
            int u = to[e];
            if (visited[u]== -1){
                heap_push(&h,w[e],u);
            }
        }
    }
    long long ans = sum-mx;
    printf("%lld\n",ans);

    free(head);free(to);free(w);free(next);
    free(visited);free(h.a);
    return 0;
}