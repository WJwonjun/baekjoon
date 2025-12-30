#include <iostream>
#include <tuple>
#include <queue>
#include <set>
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
    set<int> s;
    s.insert(a);
    q1.push({a,0});

    while(q1.empty()==false){
        auto[brid,cnt] = q1.front();
        q1.pop();
        if(brid==b) {
            cout << cnt << endl;
            return 0;
        }
        int jump = bridge[brid-1];
        for(int i=brid-jump;i>0;i-=jump){
            if(s.count(i)==0) {
                q1.push({i,cnt+1});
                s.insert(i);
            }
        }
        for(int i=brid+jump;i<=N;i+=jump){
            if(s.count(i)==0) {
                q1.push({i,cnt+1});
                s.insert(i);
            }
        }

    }
    cout << -1 << endl;
}