#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	// 코드 작성
	int X,b;
	vector<int> numlist;
	cin >> X >> b;
	
	// X: 음, 0, 양
	// b: 양, 음

	// X가 0이면 항상 0 리턴
	// 따라서 b가 양 일 때 -> X가 음 or 양  
		// X가 음수면 그냥 답에 -붙이기
		// 나머지를 이용해 일의 자리부터 구하기

	if(X==0) { // X가 0인 경우
		cout << 0 << endl;
	}
	else if(b > 0) {
    int tmp = abs(X);
    while (tmp > 0) {
        numlist.push_back(tmp % b);
        tmp /= b;
    }
    reverse(numlist.begin(), numlist.end());
    
    if(X < 0) cout << "-";
    for(auto elem : numlist) cout << elem;
    cout << endl;
	}
	
	else { 
		// -52 = 4 -8 +16 +64 -128
		while(X!=0){
			int rem = X % b;
			X /= b;

			if(rem<0){
				rem+=abs(b);
				X+=1;
			}
			numlist.push_back(rem);
		}
		reverse(numlist.begin(), numlist.end());
		for(auto elem: numlist){
			cout << elem ;
		}

		cout << endl;
	}

	return 0;
}