#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

const int MAX = 1000000;
bitset<MAX + 1> is_prime;
vector<int> primes;

void fastSieve() {
    is_prime.set();
    is_prime[0] = is_prime[1] = 0;
    for (int i = 2; i * i <= MAX; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAX; j += i)
                is_prime[j] = 0;
        }
    }
    for (int i = 2; i <= MAX; i++) {
        if (is_prime[i]) primes.push_back(i);
    }
}

pair<int, int> find_two_primes(int K) {
    if (K < 4) return {0, 0};
    for (int p : primes) {
        if (p > K / 2) break; 
        if (is_prime[K - p]) return {p, K - p};
    }
    return {0, 0};
}

void get_4_nums(int N) {
    if (N < 8) {
        cout << -1 << endl;
        return;
    }

    for (int i = 0; i < primes.size(); i++) {
        int p1 = primes[i];
        if (p1 * 4 > N) break; // p1이 평균보다 커지면 중단

        for (int j = i; j < primes.size(); j++) {
            int p2 = primes[j];
            int remain = N - p1 - p2;
            if (remain < 4) break;

            pair<int, int> p34 = find_two_primes(remain);
            if (p34.first != 0) {
                cout << p1 << " " << p2 << " " << p34.first << " " << p34.second << endl;
                return;
            }
        }
    }
    cout << -1 << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    fastSieve();

    int N;
    if (cin >> N) {
        get_4_nums(N);
    }

    return 0;
}