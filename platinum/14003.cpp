#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	// 코드 작성
	int N;
	cin >> N;
	vector<int> nums(N);
	vector<int> parent(N,-1);
	for(int i=0;i<N;i++){
		cin >> nums[i];
		parent[i] = i;
	}

	vector<int> maps;

	for (int i = 0; i < N; i++) {
        // maps에 인덱스가 들어있으므로, 비교 함수를 통해 nums[인덱스]와 nums[i]를 비교합니다.
        auto it = lower_bound(maps.begin(), maps.end(), nums[i], [&](int idx, int val) {
            return nums[idx] < val;
        });
		if(it == maps.end()) { // 맨 뒤에 push 하는 경우
			if(!maps.empty()){
				parent[i] = maps.back();
			}
			maps.push_back(i);
		}else{	
			*it = i;
			if(it != maps.begin()){ // 중간값 수정하는 경우
				parent[i] = *prev(it);
			}else parent[i] = i; // 맨 앞의 값 수정하는 경우
		}
	}

	cout << maps.size() << endl;
	vector<int> ans;
	if (!maps.empty()) {
        int cur = maps.back();
        while (true) {
            ans.push_back(nums[cur]); // 실제 값을 저장
            if (cur == parent[cur]) break;
            cur = parent[cur];
        }
    }
	for (auto it = ans.rbegin(); it != ans.rend(); ++it) {
        std::cout << *it << " ";
    }


	return 0;
}