#include <iostream>
using namespace std;

int parent[1000001];
int cnt[1000001];

int find(int n){
	if(n==parent[n]) return n;
	return parent[n] = find(parent[n]);
}

void unite(int i, int j){
	int iroot = find(i);
	int jroot = find(j);

	if(iroot!=jroot){
		parent[iroot] = jroot;
		cnt[jroot] +=cnt[iroot];
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	// 코드 작성
	for(int i=1;i<=1000000;i++){
		parent[i] = i;
		cnt[i] = 1;
	}

	int N;
	cin >> N;
	for(int i=0;i<N;i++){
		char c;
		cin >> c;

		if(c=='I'){
			int a,b;
			cin >> a >> b;
			unite(a,b);
		}
		else{
			int a;
			cin >> a;
			cout << cnt[find(a)] << "\n";
		}
	}
	return 0;
}