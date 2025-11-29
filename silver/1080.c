#include <stdio.h>

int main(){
    int N, M;
    scanf("%d %d", &N, &M);

    char A[N][M];
    char B[N][M];
    int  C[N][M];

    // A 입력 (문자로)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf(" %c", &A[i][j]);
            A[i][j] -= '0';
        }
    }

    // B 입력 & C 계산
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf(" %c", &B[i][j]);
            B[i][j] -= '0';
            C[i][j] = (A[i][j] == B[i][j] ? 0 : 1);
        }
    }
    int cnt=0;
    for (int i = 0; i < N-2; i++) {
        for (int j = 0; j < M-2; j++) {
            if(C[i][j]==1){
                for(int di=0;di<3;di++){
                    for(int dj=0;dj<3;dj++){
                        C[i+di][j+dj]=(C[i+di][j+dj] ? 0 : 1);
                    }
                }
                cnt++;
            }
    }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++)
            if (C[i][j]==1){
                printf("-1");
                return 0;
            }
    }
    printf("%d",cnt);

}

// 왼쪽+위부터 내려가면서 다른지 검사. 만약 다르면 무조건 그 칸은 왼쪽 위로 보는 윈도우를 변환해야 함 (그 칸은 다시 볼 일 없음)