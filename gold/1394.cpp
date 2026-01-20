#include <iostream>
#include <string>

using namespace std;

// 문제에서 요구하는 나머지 값
const int MOD = 900528;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string kw, pw;

    if (!(cin >> kw >> pw)) return 0;

    int n = kw.length(); 
    
    // 1. 각 문자가 몇 번째 순서인지 미리 저장 (O(kw.length))

    int value_map[256] = {0};
    for (int i = 0; i < n; i++) {

        value_map[(unsigned char)kw[i]] = i + 1;
    }

    long long ans = 0;

    // 2. 암호를 한 글자씩 확인하며 계산 (O(pw.length))
    for (int i = 0; i < (int)pw.length(); i++) {
        // 핵심 로직: 이전 결과에 전체 문자 개수(n)를 곱하고 
        // 현재 문자의 순서를 더합니다.
        ans = (ans * n + value_map[(unsigned char)pw[i]]) % MOD;
    }

    // 3. 최종 결과 출력
    cout << ans << endl;

    return 0;
}