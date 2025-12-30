#include <iostream>
#include <tuple>
#include <queue>
#include <vector>

using namespace std;
int main(){
    int N,a,b;
    cin >> N;

    vector<int> bridge(N);
    for(int i=0;i<N;i++){
        cin >> bridge[i];
    }
    cin >> a >> b;
    if(a==b){
        cout << 0 << endl;
        return 0;
    }

    queue<tuple<int, int>> q1;
    vector<bool> visited(N + 1, false);

    visited[a]=true;
    q1.push({a,0});

    while(q1.empty()==false){
        auto[cur,cnt] = q1.front();
        q1.pop();
        if(cur==b) {
            cout << cnt << endl;
            return 0;
        }
        int jump = bridge[cur-1];
        for(int next = cur + jump; next <= N; next += jump){
            if(!visited[next]) {
                visited[next] = true;
                q1.push({next, cnt + 1});
            }
        }

        for(int next = cur - jump; next >= 1; next -= jump){
            if(!visited[next]) {
                visited[next] = true;
                q1.push({next, cnt + 1});
            }
        }
    }
    cout << -1 << endl;
}