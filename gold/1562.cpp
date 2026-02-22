#include <iostream>
using namespace std;

int main() {
	// 코드 작성
	int N;
	cin >> N;
	int dp[101][10][1024] = {0,} ;// N번째 자리수, 마지막 숫자, 비트마스크




	for(int i=0;i<N;i++){
		for(int j=0;j<10;j++){
			if(i==0 && j!=0){
				dp[i+1][j][1<<j] = 1;
			}
			if(i>=1){
				for(int bit=0;bit<1024;bit++){
				if (dp[i][j][bit] == 0) continue;
				//if(dp[i-1][j][bit]!=0) cout << i-1 << " " << j << " "<< bit << " " << dp[i-1][j][bit] << endl;
				if(j>0){
					int next_bit = bit | (1 << (j-1));
					dp[i+1][j-1][next_bit] += dp[i][j][bit];
					dp[i+1][j-1][next_bit] %= 1000000000;
				}
				if(j<9){
					int next_bit = bit | (1 << (j+1));
					dp[i+1][j+1][next_bit] += dp[i][j][bit];
					dp[i+1][j+1][next_bit] %= 1000000000;
				}
			}
			}
		}
	}
	
	int cnt = 0;
	for(int j=0;j<10;j++){
		cnt += dp[N][j][1023];
		cnt %= 1000000000;
		//cout << dp[N][j][1023] << endl;
 	}

	cout << cnt << endl;
	// long long check = 0;
	// for(int j=0;j<10;j++){
	// 	for(int i=1;i<=40;i++){
	// 		check+=dp[i][j][1023];
	// 	}
	// }
	//cout << check << endl;
	
	return 0;
}