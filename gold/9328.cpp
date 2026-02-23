#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <cctype>

using namespace std;

char maps[105][105];
bool visited[105][105];
int dy[4] = {0,0,1,-1}, dx[4] = {1,-1,0,0};

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int N; cin >> N;

    while(N--) {
        int R, C, cnt = 0;
        cin >> R >> C;

        // 1. 맵 초기화 (패딩 포함)
        for(int i=0; i<=R+1; i++) {
            for(int j=0; j<=C+1; j++) {
                maps[i][j] = '.';
                visited[i][j] = false;
            }
        }

        // 2. 실제 데이터 입력 (1, 1부터 시작)
        for(int i=1; i<=R; i++) {
            string temp; cin >> temp;
            for(int j=1; j<=C; j++) maps[i][j] = temp[j-1];
        }

        string keys; cin >> keys;
        set<char> keylist;
        if(keys != "0") {
            for(char k : keys) keylist.insert(k);
        }

        queue<pair<int,int>> Q;
        map<char, vector<pair<int,int>>> gatelist;

        Q.emplace(0, 0);
        visited[0][0] = true;

        while(!Q.empty()){
            auto [y, x] = Q.front(); Q.pop();

            for(int i=0; i<4; i++){
                int ny = y + dy[i], nx = x + dx[i];

                if(ny < 0 || ny > R+1 || nx < 0 || nx > C+1) continue;
                if(visited[ny][nx] || maps[ny][nx] == '*') continue;

                char cur = maps[ny][nx];
                visited[ny][nx] = true;

                if(cur == '.') {
                    Q.emplace(ny, nx);
                } else if(cur == '$') {
                    cnt++;
                    Q.emplace(ny, nx); 
                } else if(islower(cur)) {
                    keylist.insert(cur);
                    Q.emplace(ny, nx);
                    char gate = toupper(cur);
                    if(gatelist.count(gate)) {
                        for(auto [gy, gx] : gatelist[gate]) {
                            Q.emplace(gy, gx);
                        }
                        gatelist.erase(gate);
                    }
                } else if(isupper(cur)) {
                    if(keylist.count(tolower(cur))) {
                        Q.emplace(ny, nx);
                    } else {
                        gatelist[cur].push_back({ny, nx});
                    }
                }
            }
        }
        cout << cnt << "\n";
    }
    return 0;
}