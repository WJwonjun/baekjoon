#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct State{
	pair<int, int> pos;
	int cnt;
	vector<vector<bool>> vis;
};

int dy[] = {-1,1,0,0};
int dx[] = {0,0,-1,1};

int main() {
	int R, C, K;
	cin >> R >> C >> K;
	
	vector<string> maps(R);
	for (int i = 0; i < R; i++) {
        cin >> maps[i];
    }
	
	queue<State> q;
	vector<vector<bool>> initial_vis(R, vector<bool>(C,false));

	initial_vis[R-1][0] = true;
	q.push({{R-1, 0}, 1, initial_vis});

	int ans= 0 ;
	while(!q.empty()){
		State cur = q.front();
		q.pop();
		
		int y = cur.pos.first;
		int x = cur.pos.second;

		if(cur.cnt==K) {
			if(y==0 && x==C-1) ans++;
			continue;
		}
		
		for(int i=0;i<4;i++){
			int ny = y + dy[i];
			int nx = x + dx[i];

			if(ny>=0 && ny < R && nx >=0 && nx < C && maps[ny][nx]!='T'){
				if(!cur.vis[ny][nx]){
					vector<vector<bool>> next_vis = cur.vis;
					next_vis[ny][nx]= true;
					q.push({{ny, nx}, cur.cnt + 1, next_vis});
				}
			}
		}
	}
	cout << ans << endl;
	
}