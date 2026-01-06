#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);
	
	int N;
	cin >> N;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	int trash;
	for(int i=0;i<N;i++){
		int a,b,c;
		cin >> a >> b >> c;
		pq.push({b,c});
	}

	int cnt = 0;
	priority_queue<int, vector<int>, greater<int>> nums; //제일 빨리 끝나는 수업이 top에 오게 됨.
	while(!pq.empty()){
		int start = pq.top().first;
		int end = pq.top().second;
		pq.pop();
		if(!nums.empty() && start >= nums.top()){ // 들어갈 수 있는 교실이 있음
			nums.pop();
		}

		nums.push(end); 
		}
	
	cout << nums.size() << endl;
	

}