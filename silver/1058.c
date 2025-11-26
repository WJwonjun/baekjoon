#include <stdio.h>
#include <stdbool.h>
#define max(x, y) ((x) > (y) ? (x) : (y))

int main(){
    int N;
    scanf("%d",&N);
    char friends[50][50];
    int max_num=0;

    for(int i=0;i<N;i++){
        scanf("%s",friends[i]);
    }

    for(int i=0;i<N;i++){
        bool check[50] = {false};

        // 1단계: i의 친구
        for(int j=0;j<N;j++){
            if (friends[i][j]=='Y') check[j]=true;
        }

        // 2단계: i의 친구(j)의 친구(k)
        for(int j=0;j<N;j++){
            if (friends[i][j]=='Y') {
                for(int k=0;k<N;k++){
                    if (friends[j][k]=='Y')
                        check[k] = true;
                }
            }
        }

        check[i] = false; // 자기자신 제외

        int cnt = 0;
        for(int x=0;x<N;x++){
            if(check[x]) cnt++;
        }

        max_num = max(max_num, cnt);
    }

    printf("%d",max_num);
}
