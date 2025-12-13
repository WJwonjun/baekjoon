#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> a(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());


    for (int i = N - 1; i >= 2; i--) {
        long long x = a[i - 2];
        long long y = a[i - 1];
        long long z = a[i];


        if (a[i - 2] + a[i - 1] > a[i]) {
            cout << a[i - 2] + a[i - 1] + a[i] << '\n';
            return 0;
        }
    }

    cout << -1 << '\n';
    return 0;
}
