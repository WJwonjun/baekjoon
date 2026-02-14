#include <iostream>
#include <set>
using namespace std;

int parent[10001];
int costlist[10001];

int find(int i){
	if(parent[i]==i) return i;
	return parent[i] = find(parent[i]);
}

void unite(int i, int j){
	int iroot = find(i);
	int jroot = find(j);
	if(iroot!=jroot ){
		if(costlist[iroot]>costlist[jroot]) parent[iroot] = jroot;
		else parent[jroot] = iroot;
	}

}

int main() {
	// 코드 작성

	int N,M,c;
	cin >> N >> M >> c;

	for(int i=1;i<=N;i++){
		cin >> costlist[i];
		parent[i] = i;
	}

	for(int i=0;i<M;i++){
		int a,b;
		cin >> a >> b;
		unite(a,b);
		// for(int i=1;i<=N;i++){
		// 	cout << parent[i] << " ";
		// }
		//cout << endl;
	}





	int ans=0;
	set<int> temp;

	for(int i=1;i<=N;i++){
		int iroot = find(i);
		if(!temp.contains(iroot)){
			temp.insert(iroot);
			ans+=costlist[iroot];
		}
	}

	if(c<ans){
		cout << "Oh no" << endl;
	}
	else{
		cout << ans << endl;
	}

	return 0;
}