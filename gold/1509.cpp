#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	// 코드 작성

	string target;
	cin >> target;
	int length = target.size();
	map<int,vector<int>> pals;
	for(int center = 0; center<length-1; center++){
		int i=0;
		while(center-i-1>=0 && center+i+1<length){ // 홀수 길이 팰린드롬
			if(target[center-i-1]!=target[center+i+1]) break;
			i++;
			if(i>0) pals[center+i].push_back(center-i);
		}
		

		if(target[center]==target[center+1]){
			int i=0;
			while(center-i-1>=0 && center+2+i<length){
				if(target[center-i-1]!=target[center+2+i]) break;
				i++;
				pals[center+1+i].push_back(center-i);
			}
			pals[center+1].push_back(center);
		}
	}

	vector<int> dp(length+1,2500);
	dp[0] = 0; // 실제 string은 dp에 1~N으로 입력됨

	for(int i=1;i<=length;i++){
		for(int start : pals[i-1]){ 
			//cout << start << " " << i-1 << endl;
			dp[i] = min({dp[i],dp[i-1]+1, dp[start] + 1});
		}
		dp[i] = min(dp[i],dp[i-1]+1);
		//cout << dp[i] << endl;
	}
	cout << dp[length] << endl;

	return 0;
}