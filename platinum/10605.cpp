#include <iostream>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;


struct Dragon {
    long long s, n;
};

int main() {
	// 코드 작성

	while(true){
		int ans=0;
		int N,M,K;
		cin >> N >> M >> K;
		vector<bool> visited(N+1, false);
		if(N==0 && M==0 && K==0) break; // 도시, 다리, 드래곤
		
		map<int,vector<int>> bridges;
		for(int i=0;i<M;i++){ // 다리 입력받기
			int a,b;
			cin >> a >> b;
			bridges[a].push_back(b);
			bridges[b].push_back(a);
		}

		vector<vector<Dragon>> city_dragons(N + 1);
        for (int i = 0; i < K; i++) {
            int c;
            int s, n;
            cin >> c >> s >> n;
            city_dragons[c].push_back({s, n});
        }


		for(int i=1;i<=N;i++){
			if (!visited[i]) {
                visited[i] = true;
                queue<int> Q;
                Q.push(i);
                
                vector<Dragon> comp_dragons;
                
                // BFS로 연결된 클러스터(컴포넌트) 내의 모든 드래곤 수집
                while (!Q.empty()) {
                    int cur_city = Q.front();
                    Q.pop();
                    
                    for (auto& d : city_dragons[cur_city]) {
                        comp_dragons.push_back(d);
                    }
                    
                    for (int next_city : bridges[cur_city]) {
                        if (!visited[next_city]) {
                            visited[next_city] = true;
                            Q.push(next_city);
                        }
                    }
                }
        if(!comp_dragons.empty()){
			sort(comp_dragons.begin(), comp_dragons.end(), [](const Dragon& a, const Dragon& b) {return a.n > b.n;});

				int cur_worker = 0;
				for(auto &d : comp_dragons){
					int first = d.s; // 처음부터 배치한다고 했을 때 필요한 양
					int second = d.n - cur_worker+1; // 나중에 와서 잡는다고 했을 때 추가할 양
					//cout << first << " " << second << endl;
					if(second<=0) continue; // 이미 cur_worker 충분해서 필요없음
					else cur_worker += min(first,second);
				}
				ans += cur_worker;
			}	
		}
    }
		cout << ans << endl;
	}
    
		return 0;
	}