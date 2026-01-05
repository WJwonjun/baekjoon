#include <iostream>
#include <string>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int N, K;
    if (!(cin >> N >> K)) return 0; // Good practice to check if input succeeds

    // 1. Initialize the vector with size N
    string start = "";

	for(int i = 0; i < N; i++) {
		int x; cin >> x;
		start += to_string(x); // 숫자를 문자열로 변환하여 저장
	}

	string target = start;
	sort(target.begin(), target.end());

	int cnt=0;
	queue<pair<string, int>> Q;
	set<string> visited;
	Q.push({start,0});
	visited.insert(start);

	int possible = N-K;
	while(!Q.empty()){
		string cur = Q.front().first;
		int count = Q.front().second;
		Q.pop();

		if(cur==target){
			cout << count << endl;
			return 0;
		}
		else{
			for(int i=0;i<=possible;i++){
				string next = cur;
				reverse(next.begin()+i,next.begin()+i+K);
				if(visited.find(next)==visited.end()){
					visited.insert(next);
					Q.push({next,count+1});
				}
			}
		}

	}

	cout << -1 << endl;
    return 0;
}