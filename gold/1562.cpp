#include <iostream>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <cctype>
using namespace std;

char maps[105][105];
bool visited [105][105];
int dy[4] = {0,0,1,-1};
int dx[4] = {1,-1,0,0};

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int N;
    cin >> N;
    

    for(int k=0;k<N;k++){
        int R,C,cnt=0;
        cin >> R >> C;

        queue<pair<int,int>> Q;
        map<char,vector<pair<int,int>>> gatelist;
        set<char> keylist;
        memset(visited, false, sizeof(visited));

        for(int i=0; i<R; i++) {
            string temp; cin >> temp;
            for(int j=0; j<C; j++) {
                maps[i][j] = temp[j];
            }
        }

        string keys;
        cin >> keys;
        if(keys!="0"){
            for (char k : keys) keylist.insert(k);
        }

        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if(i==0 || i==R-1 || j==0 || j==C-1) {
                    if(maps[i][j] == '*' || visited[i][j]) continue;
                    
                    char cur = maps[i][j];
                    // 입구에서 바로 수행해야 할 작업들
                    if(islower(cur)) {
                        keylist.insert(cur);
                        char targetGate = toupper(cur);
                        if (gatelist.count(targetGate)) {
                            for (auto [gy, gx] : gatelist[targetGate]) {
                                Q.emplace(gy, gx);
                            }
                            gatelist.erase(targetGate);
                        }
                    }
                    
                    else if(cur == '$') cnt++;
                    else if(isupper(cur)) {
                        if(!keylist.contains(tolower(cur))) {
                            gatelist[cur].push_back({i, j});
                            visited[i][j] = true; 
                            continue; // 열쇠 없으면 일단 못 들어감
                        }
                    }
                    
                    Q.emplace(i, j);
                    visited[i][j] = true;
                }
            }
        }

    

    while(!Q.empty()){
        auto[y,x] = Q.front();
        Q.pop();
        for(int i=0;i<4;i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(0<=ny && ny<R && 0<=nx && nx<C){
                if(visited[ny][nx]==false){
                    visited[ny][nx] = true;
                    
                    if(maps[ny][nx]=='.') {
                        Q.emplace(ny,nx);
                    }else if('A'<=maps[ny][nx] && maps[ny][nx]<='Z') {
                        if(keylist.contains(tolower(maps[ny][nx]))){
                            maps[ny][nx] = '.';
                            Q.emplace(ny,nx);
                        }else{
                            gatelist[maps[ny][nx]].emplace_back(ny,nx);
                        }
                    }else if('a'<=maps[ny][nx] && maps[ny][nx]<='z') {
                        keylist.insert(maps[ny][nx]);
                        Q.emplace(ny,nx);
                        for(auto [g_y,g_x]:gatelist[toupper(maps[ny][nx])]){
                            maps[g_y][g_x] = '.';
                            Q.emplace(g_y,g_x);
                        }
                    }else if(maps[ny][nx]=='$'){
                        cnt++;
						Q.emplace(ny,nx);
                    }

                }
            }
        }
    }


    cout << cnt << "\n";

    }
    return 0;
}