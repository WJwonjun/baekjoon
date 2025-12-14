#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N,L;
    cin >> N >> L;
    
    vector<int> nums(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }
    sort(nums.begin(),nums.end());

    int cur = 0;
    int cnt = 0;
    while(cur<N){
        int start = nums[cur];
        while(cur<N && nums[cur] <= start+L-1){
            cur++;
        }
        cnt++;
    }

    cout << cnt << endl;
}