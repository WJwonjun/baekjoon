#include <iostream>

using namespace std;

int main() {
    // 입출력 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long X, K;
    cin >> X >> K;

    long long Y = 0;       // 우리가 찾고자 하는 K번째 작은 값
    long long k_bit = 0;   // K의 현재 비트 위치
    long long x_bit = 0;   // X를 검사할 비트 위치

    // K의 모든 비트를 Y의 빈 공간에 다 채울 때까지 반복
    while ((K >> k_bit) > 0) {
        // X의 x_bit 자리가 0(빈칸)인지 확인
        if (!((X >> x_bit) & 1)) {
            // X가 0인 자리에 K의 k_bit번째 비트를 넣어줌
            if ((K >> k_bit) & 1) {
                Y |= (1LL << x_bit);
            }
            // K의 비트를 하나 썼으므로 다음 비트로 이동
            k_bit++;
        }
        // X의 다음 자리를 검사하기 위해 이동
        x_bit++;
    }

    cout << Y << endl;

    return 0;
}