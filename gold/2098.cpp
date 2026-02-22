#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int maps[16][16];
int dp[16][1<<16];

struct state{
	unsigned int cur:4;
	int cost;
	unsigned int visited:16;

	state(int c, int co, int v) 
        : cur(c), cost(co), visited(v) {}
	
	bool operator>(const state& other) const {
        return cost > other.cost;
    }
};


int main() {
	// 코드 작성
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	fill(&dp[0][0], &dp[0][0] + 16 * (1 << 16), 1e9);

	int N;
	cin >> N;
	
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			cin >> maps[i][j];
		}
	}
	priority_queue<state, vector<state>, greater<state>> Q;
	dp[0][1 << 0] = 0; // 시작점 초기화 필수
	Q.push({0, 0, 1 << 0});

	int ans = 1e9;
	int max_bit = (1 << N) - 1;



	while(!Q.empty()){
		state s = Q.top();
		Q.pop();
		//cout << start << " " << cur << " " << cost << " " << visited << endl;
		if (s.cost > dp[s.cur][s.visited]) continue;

		if(s.visited==max_bit) {
			if(maps[s.cur][0]!=0) ans = min(ans,s.cost+maps[s.cur][0]);
			continue;
		}

		for(int next=0;next<N;next++){
			int next_bit = s.visited|(1<<next);
			int next_cost = s.cost+maps[s.cur][next];
			if(s.visited != next_bit && 0<maps[s.cur][next] && next_cost<dp[next][next_bit]){ // not visited && can go
				dp[next][next_bit] = next_cost;
				Q.push({next,next_cost,next_bit});
			}
		}
 	}
	cout << ans << endl;
	return 0;
}