#include <iostream>
#include <vector>
#include <map>
using namespace std;

int parent[201];

int find(int cur){
	if(parent[cur] == cur) return cur;
	return parent[cur] = find(parent[cur]);
}

void unite(int i, int j){
	int iroot = find(i);
	int jroot = find(j);
	if(iroot!=jroot){
		parent[iroot] = jroot;
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N,M;
	cin >> N;
	cin >> M;
	for(int i=1;i<=N;i++){
		parent[i] = i;
	}
	
	//vector<vector<int>> temp(N, vector<int>(N, 0));

	int temp;
	for(int i=1;i<=N;i++){
		for(int j=1;j<=N;j++){
			cin >> temp;
			if(i<=j && temp==1){
				unite(i,j);
				
			}
		}
	}

	int cur, past;
	for(int i=0;i<M;i++){
		cin >> cur;

		if(i!=0){
			if(find(cur)!=find(past)) {
				cout << "NO";
				return 0;
			}
		}

		past = cur;
	}

	cout << "YES" << endl;
	return 0;
}