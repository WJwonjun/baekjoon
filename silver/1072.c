#include <stdio.h>

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);

    int z = (b * 100) / a;

    if (z >= 99) {  // 승률이 99 이상이면 절대 변하지 않음
        printf("-1");
        return 0;
    }

    long long left = 1;
    long long right = 1000000000;
    long long result = -1;

    while (left <= right) {
        long long mid = (left + right) / 2;
        int newZ = ((b + mid) * 100) / (a + mid);

        if (newZ > z) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    printf("%lld", result);
    return 0;
}