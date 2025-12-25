#include <algorithm>
#include <iostream>
using namespace std;

long long dist2(int x1, int y1, int x2, int y2) {
    long long dx = x1 - x2;
    long long dy = y1 - y2;
    return dx*dx + dy*dy;
}

bool isSquare(int x[4], int y[4]) {
    long long int d[6];
    int idx = 0;

    // 모든 점 쌍의 거리^2 (6개)
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            d[idx++] = dist2(x[i], y[i], x[j], y[j]);
        }
    }

    sort(d, d + 6);

    // 0이면 점이 겹친 것
    if (d[0] == 0) return false;

    // 변 4개가 같고
    for (int i = 0; i < 4; i++) {
        if (d[i] != d[0]) return false;
    }

    // 대각선 2개가 같고
    if (d[4] != d[5]) return false;

    // 대각선^2 = 변^2 * 2
    if (d[4] != 2 * d[0]) return false;

    return true;
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int x[4], y[4];
        for (int j = 0; j < 4; j++) {
            cin >> x[j] >> y[j];
        }
        cout << (isSquare(x, y) ? 1 : 0) << '\n';
    }
}