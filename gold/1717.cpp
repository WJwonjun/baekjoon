#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int parent[1000001];


int find(int a){
	if(parent[a]==a) return a;
	return parent[a] = find(parent[a]);
}

void unite(int a, int b) {
    int rootA = find(a);
    int rootB = find(b);
    
    if (rootA != rootB) { // 둘의 루트가 다를 때만 합침
        parent[rootB] = rootA;
    }
}

int main() {
	// 코드 작성
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int N, M;

	cin >> N >> M;


	for(int i=0;i<=N;i++){
		parent[i] = i;
	}

	for(int i=0;i<M;i++){
		int c,a,b;
		cin >> c >> a >> b;
		if(c==0){
			unite(a,b);
		}
		else{
			if(find(a)==find(b)) cout << "YES\n" ; 
			else cout << "NO\n"; 
		}
	}
	
	return 0;
}