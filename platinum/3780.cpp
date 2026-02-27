#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

int parent[20001]={0,};

int length[20001]={0,};

int find(int i){
	if(parent[i]==i) return i;

	int root = find(parent[i]);
	length[i] += length[parent[i]];
	return parent[i] = root;
}

void unite(int i, int j){
		parent[i] = j;
		length[i] = abs(i-j)%1000;
}


int main() {
	// 코드 작성
	int K;
	cin >> K;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	for(int _i=0;_i<K;_i++){
		int N;
		cin >> N;
		iota(parent, parent + N+1, 0);
		fill(length, length + N+1, 0);

		while(true){
			char cmd;
			cin >> cmd;
			if(cmd=='E'){
				int c;
				cin >> c;
				find(c);
				cout << length[c] << "\n";
			}else if(cmd=='I'){
				int a,b;
				cin >> a >> b;
				unite(a,b);
			}else break;
		}
	}
	return 0;
}