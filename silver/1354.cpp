#include <iostream>
#include <queue>
#include <map>
using namespace std;

long long P, Q, X, Y;
map<long long, long long> memo;

long long solve(long long n) {
    // 1. 기저 조건: n이 0 이하이면 문제의 조건에 따라 1을 반환 (보통 이런 유형은 1부터 시작)
    if (n <= 0) return 1;

    // 2. 이미 계산한 적이 있다면 그 값을 즉시 반환 (메모이제이션)
    if (memo.count(n)) return memo[n];

    // 3. 점화식 계산: f(n) = f(n/P - X) + f(n/Q - Y)
    return memo[n] = solve(n / P - X) + solve(n / Q - Y);
}

int main(){
	long long N;
    if (!(cin >> N >> P >> Q >> X >> Y)) return 0;

    // 결과 출력
    cout << solve(N) << endl;

    return 0;
}