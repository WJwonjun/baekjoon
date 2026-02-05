#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <math.h>
using namespace std;

int main() {
	int N;
	int dictArray[10][12]= {0};
	cin >> N ;
	vector<bool> zero_possible(10, true);

	for(int i=0;i<N;i++){
		string temp;
		cin >> temp;

		for(int j=temp.size()-1;j>=0;j--){
			int row = temp[j]-'A';
			int power = temp.size() - 1 - j;
            dictArray[row][power]++;
			if(j==0){
				zero_possible[row] = false;
			}
		}
	}

	priority_queue<pair<long long,int>> pq;
	long long min=1e13;
	int zero = -1;

	for(int i=0;i<10;i++){
		long long cur=0;
		for(int j=0;j<12;j++){
			if (dictArray[i][j] > 0) {

                cur += (long long)(dictArray[i][j] * pow(10, j));
            }
		}	
		if(cur>0) {
			if((cur<min || min==-1) && zero_possible[i] ){
				min = cur;
				zero = i;
			}
			pq.push({cur,i});
		}
		//cout << cur << endl;
	}

	if(pq.size()!=10){zero = -1;}

	long long ans=0;
	long long give = 9;

	while(!pq.empty()){
		int i = pq.top().second;
		long long num = pq.top().first;
		pq.pop();
		//cout << pq.top() << endl;
		if(i==zero){
			continue;
		}
		ans += num*give;
		give--;

	}
	cout << ans << endl;
}