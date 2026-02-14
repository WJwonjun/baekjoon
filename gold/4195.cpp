#include <iostream>
#include <map>
#include <string>
using namespace std;

#define MAX_SIZE 200001
int parent[MAX_SIZE];
int cnt[MAX_SIZE];

int find(int i){
	if(i==parent[i]) return i;
	return parent[i] = find(parent[i]);
}

int unite(int i,int j){
	int iroot = find(i);
	int jroot = find(j);

	if(iroot!=jroot){
		parent[iroot] = jroot;
		cnt[jroot] += cnt[iroot];
	}
	return cnt[jroot];
}

map<string, int> namelist;
int pplcnt = 0;

int nametoid(string& s){
	if(namelist.count(s)) return namelist[s];
	return namelist[s] = ++pplcnt;
}



int main() {
	// 코드 작성
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int N,F;

	
	cin >> N;
	for(int i=0;i<N;i++){
		cin >> F;
		

		for(int i=0;i<100000;i++){
		parent[i] = i;
		cnt[i] = 1;
		} //준비 작업

		for(int j=0;j<F;j++){
			string a,b;
			int id1,id2;
			cin >> a >> b;
			id1 = nametoid(a);
			id2 = nametoid(b);
			//cout << id1 << " " << id2 ;
			cout << unite(id1,id2) << "\n";

		}
		
	}
	return 0;
}