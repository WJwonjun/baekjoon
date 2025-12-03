#include <stdio.h>
#include <string.h>

int main(void){
    int N;
    scanf("%d", &N);

    // 단어 길이가 최대 50이니까 널문자까지 51 필요
    char string[50][51];

    for (int i = 0; i < N; i++) {
        scanf("%50s", string[i]);   // 안전하게 최대 50글자만 읽기
    }

    // 1) 중복 제거 (뒤에 나오는 중복을 비우기)
    for (int i = 0; i < N; i++) {
        if (string[i][0] == '\0') continue;
        for (int j = i + 1; j < N; j++) {
            if (string[j][0] == '\0') continue;
            if (strcmp(string[i], string[j]) == 0) {
                string[j][0] = '\0';
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        if (string[i][0] != '\0') cnt++;
    }

    // 3) 각 i가 다른 j의 접두사인지 검사
    for (int i = 0; i < N; i++) {
        if (string[i][0] == '\0') continue;   // 이미 제거된 건 패스

        int len_i = strlen(string[i]);
        int is_prefix = 0;

        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            if (string[j][0] == '\0') continue;

            int len_j = strlen(string[j]);

            // i가 j보다 짧을 때만 접두사 가능
            if (len_i >= len_j) continue;

            // i가 j의 접두사인지 확인
            if (strncmp(string[j], string[i], len_i) == 0) {
                is_prefix = 1;
                break;
            }
        }

        if (is_prefix) {
            cnt--;
        }
    }

    printf("%d\n", cnt);
    return 0;
}
