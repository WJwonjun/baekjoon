#include <stdio.h>

#define MAX_NUM 1000000000

int main() {
    long long N;
    int L;

    scanf("%lld %d", &N, &L);

    long long ans_start = -1;
    int ans_num = -1;

    for (int j = L; j <= 100; j++) {
        ans_start = -1;
        ans_num = -1;

        long long lo = 0;
        long long hi = MAX_NUM;

        while (lo <= hi) {
            long long mid = (lo + hi) / 2;

            // mid부터 j개 연속된 수의 합 계산
            long long cnt = (long long)j * mid + (long long)j * (j - 1) / 2;

            if (cnt == N) {
                ans_start = mid;
                ans_num = j;
                break;
            } else if (cnt < N)
                lo = mid + 1;
            else
                hi = mid - 1;
        }

        if (ans_start != -1) break;
    }

    if (ans_start == -1)
        printf("%d", -1);
    else {
        for (int i = 0; i < ans_num; i++)
            printf("%lld ", ans_start + i);
    }

    return 0;
}
