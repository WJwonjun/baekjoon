#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;


struct Map{
	int size;
	vector<vector<int>> space;

	Map(int n): size(n),space(n, vector<int>(n,0)){}
};

vector <int> dy = {-1,1,0,0};
vector <int> dx = {0,0,1,-1};

int main() {
	ios::sync_with_stdio(0); 
	cin.tie(0);
	
	int pro=1;
	while(true){
		int n;
		cin >> n;
		if(n==0) break;
		Map myMap(n);
		for (int i = 0; i < n; i++) {
    		for (int j = 0; j < n; j++) {
        cin >> myMap.space[i][j];
			}
		}
		
		int cnt = 1e9;
		const int INF = 1e9; // 10억 (충분히 큰 값)
		vector<vector<int>> dist(n, vector<int>(n, INF));
		dist[0][0] = myMap.space[0][0];
		priority_queue<tuple<int,int,int>, vector<tuple<int, int, int>>, greater<>> min_pq;
		min_pq.emplace(myMap.space[0][0],0,0);
		 
		while(!min_pq.empty()){
			auto[cur,y,x] = min_pq.top();
			min_pq.pop();
			if (cur > dist[y][x]) continue;
			if(y==n-1 && x==n-1){
				cnt = min(cnt, cur);
				continue;
			}
			for(int i=0;i<4;i++){
				int ny = y+dy[i];
				int nx = x+dx[i];
				if(0<=ny && ny<n && 0<=nx && nx<n && cur+myMap.space[ny][nx]<dist[ny][nx] ){
					min_pq.emplace(cur+myMap.space[ny][nx],ny,nx);
					dist[ny][nx] = cur+myMap.space[ny][nx];
				}
			}
		}
		cout << "Problem " << pro << ": " << cnt << endl;
		pro++;
	}
	return 0;
}