#include <iostream>
#include <vector>
#include <string>
using namespace std;


int N;


vector<int> ans;
vector<vector<char>> matrix;


bool check(int index){
	int sum = 0;
	for(int i=index;i>=0;i--){
		sum+= ans[i];
		if (matrix[i][index]=='+' && sum<=0) return false;
		if (matrix[i][index]=='-' && sum>=0) return false;
		if (matrix[i][index]=='0' && sum!=0) return false;
	}
	return true;
}

void solve(int cnt){
	if(cnt==N){
		for(int i=0;i<N;i++) cout << ans[i] << " ";
		exit(0);
	}
	for(int i=-10;i<=10;i++){
		ans[cnt] = i;
		if(check(cnt)) solve(cnt+1);
	}
}

int main() {
    if (!(cin >> N)) return 0;

    // N을 입력받은 후 크기 재설정
    ans.resize(N);
    matrix.assign(N, vector<char>(N));

    string temp;
    cin >> temp;

    int idx = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i; j < N; j++) {
            matrix[i][j] = temp[idx++];
        }
    }

    solve(0);
    return 0;
}