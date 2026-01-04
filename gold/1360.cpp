#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    // 입출력 속도 향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    // (시간 t, 그 시점의 완성된 문자열)을 저장
    vector<pair<int, string>> history;
    history.push_back({-1, ""}); // 초기 상태 (0초 이전)

    for (int i = 0; i < N; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "type") {
            char c;
            int t;
            cin >> c >> t;
            // 이전 시점의 문자열 + 새로운 문자
            string next_str = history.back().second + c;
            history.push_back({t, next_str});
        } 
        else if (cmd == "undo") {
            int duration, t;
            cin >> duration >> t;
            
            int target_time = t - duration - 1; // 'duration' 동안 되돌리므로 그 직전 시간
            
            // target_time보다 작거나 같은 시간 중 가장 최신 상태 찾기 (뒤에서부터 탐색)
            string restored_str = "";
            for (int j = (int)history.size() - 1; j >= 0; j--) {
                if (history[j].first <= target_time) {
                    restored_str = history[j].second;
                    break;
                }
            }
            history.push_back({t, restored_str});
        }
    }

    // 가장 마지막에 저장된 문자열이 최종 결과
    cout << history.back().second << endl;

    return 0;
}