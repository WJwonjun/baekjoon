#include <stdio.h>

int main() {
    int T, N, M;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        scanf("%d %d", &N, &M);

        if (N > M - N)  // 조합의 대칭성 이용: C(M, N) == C(M, M-N)
            N = M - N;

        long long ans = 1;
        for (int j = 1; j <= N; j++) {
            ans = ans * (M - N + j) / j;
            printf("%d %d\n",(M-N+j),j);
        }

        printf("%lld\n", ans);
    }

    return 0;
}
