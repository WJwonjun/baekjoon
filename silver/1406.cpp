#include <iostream>
#include <string>
using namespace std;

int main() {
	string left, right;

	cin >> left;

	int N;
	cin >> N;

	while(N--){
		char command;
		cin >> command;

		if(command=='P'){
			char c;
			cin >> c;
			left.push_back(c);
		}
		else if(command=='L'){
			if(!left.empty()){
				right.push_back(left.back());
				left.pop_back();
			}
		}
		else if(command=='D'){
			if(!right.empty()){
				left.push_back(right.back());
				right.pop_back();
			}
		}
		else if(command=='B'){
			if(!left.empty()) left.pop_back();
		}
	}
	while(!right.empty()){
		left.push_back(right.back());
		right.pop_back();
	}

	cout << left << endl;
}