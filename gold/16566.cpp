#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int parent[4000001];
int N,M,K;

int find(int i){
	if(i==parent[i]) return i;
	return parent[i] = find(parent[i]);
}

void unite(int i, int j){
	int rootI = find(i);
	int rootJ = find(j);
	if(rootI!=rootJ) parent[rootI] = rootJ;
}


int main() {
	// 코드 작성
	ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M >> K;

    vector<int> cards(M);
    for (int i = 0; i < M; i++) {
        cin >> cards[i];
    }
    sort(cards.begin(), cards.end());
	// for (auto card:cards){
	// 	cout << card << " ";
	// }
	// cout << "\n";

	for (int i = 0; i <= M; i++) {
        parent[i] = i;
    } // i번째 카드를 사용하려고 할 때 실제 사용해야 하는 카드의 위치

	for (int i = 0; i < K; i++) {
        int q;
        cin >> q;

        auto it = upper_bound(cards.begin(), cards.end(), q);
        int idx = distance(cards.begin(), it);

        // 유니온 파인드로 실제 가용한(사용하지 않은) 인덱스 찾기
        int real_idx = find(idx);

        // 결과 출력 및 다음 인덱스와 병합 (카드 사용 처리)
        cout << cards[real_idx] << "\n";
        unite(real_idx, real_idx + 1);
		// for(int i=0;i<=M;i++){
		// 	cout << parent[i] << " ";
		// }
		// cout << "\n";
    }
	return 0;	
}