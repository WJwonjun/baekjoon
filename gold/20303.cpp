#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	// 코드 작성
	int N,M,K;
	cin >> N >> M >> K;
	vector<int> candy(N);
	//vector<pair<int,int>> packlist;
	for(int i=0;i<N;i++) cin >> candy[i];

	map<int,vector<int>> road;
	for(int i=0;i<M;i++){
		int a,b;
		cin >> a >> b;
		road[a-1].push_back(b-1);
		road[b-1].push_back(a-1);
	}
	vector<pair<int,int>> candylist; // 인원 수, 캔디 수
	vector<bool> visited(N,false);
	for(int i=0;i<N;i++){
		int cluster_candy = 0, cnt=0;
		if(visited[i]==false){
			queue<int> Q;
			Q.emplace(i);
			visited[i] = true;

			while(!Q.empty()){
				int cur = Q.front();
				Q.pop();
				cluster_candy += candy[cur];
				cnt++;
				for(const auto& next: road[cur]){
					if(visited[next]==false){
						visited[next] = true;
						Q.emplace(next);
					}
				}
			}
		}
		if(cnt!=0) candylist.push_back({cnt,cluster_candy});
	}	
	int n = candylist.size(); // 최대 3만 (각각 1명씩)
	vector<vector<int>> dp(n+ 1, vector<int>(K, 0)); 

	for(int i=1;i<=n;i++){ // i번까지 봤을 때 (가방 개수)
		int weight = candylist[i - 1].first;  // 현재 그룹 인원수
    	int value = candylist[i - 1].second;  // 현재 그룹 사탕수

		for(int j=0;j<K;j++){ // 몇명까지 수용 가능한가 (최대 비용)
			if(j>=weight) dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value); // 공간이 있는 경우: 지금 가방 넣는 경우와 넣지 않는 경우 비교
			else dp[i][j] = dp[i-1][j];
		}
	}
	cout << dp[n][K - 1] << endl;
	return 0;
}