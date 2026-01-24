#include <iostream>
#include <queue>
#include <tuple>
#include <set>
using namespace std;

int main() {
	int l,r,k;
	int cnt = 0 ;
	cin >> l >> r >> k ;
	// x*k + (k-1)*k/2*d
	// ax+bd = l or r 
	switch (k)
	{
	case 2:
		if(r<3) cnt=0;
		else if(l<3) cnt = r-3+1;
		else cnt = r-l+1;
		break;
	case 3:
		if(r<6) cnt = 0;
		else if(l<6) cnt = r/3-1; //3 제외
		else cnt = r/3 - (l-1)/3;
		break;
	case 4:
		if(r<10) cnt = 0;
		else if(l<10) {cnt = (r-10)/2+1; // 10 이상의 
			if(l<=12 && 12<=r) cnt-=1;
			
		}
		else {cnt = r/2-(l-1)/2;
			if(l<=12 && 12<=r) cnt-=1;
		}
		break;
	case 5:
		if(r<15) cnt = 0;
		else if(l<15) cnt = (r-15)/5+1;
		else cnt = r/5-(l-1)/5;

	default:
		break;
	}
	cout << cnt << endl;
	
}
// 결국 k에 대해서 가능한 수들의 목록이 정해져 있음 -> 최대 d를 구할 수 있음
// l에 해당하는 경우의 수, r에 해당하는 경우의 수 구해 그 사이 값 구하기


// k=2인 경우(3부터 전부 가능)
// 1,2 : 3
// 1,3 : 4
// 1,4 : 5

// 2,3 : 5
// 2,4 : 6

// k=3인 경우(6부터 3의 배수)
// 1,2,3: 6
// 1,3,5: 9
// 1,4,7: 12
// 1,5,9: 15

// 2,3,4: 9
// 2,4,6: 12

// 7,8,9: 24

// k=4인 경우 (10 이상의 짝수: 12 제외)
// 1,2,3,4:10
// 1,3,5,7:16
// 1,4,7,10:22
// 1,5,9,13:28
// 1,6,11,16:34
// 40

// 2,3,4,5:14
// 2,4,6,8:20
// 26
// 32
// 38

// 3,4,5,6:18
// 24
// 30
// 36

// k=5인 경우(15 이상의 5의 배수)
// 12345: 15
// 13579: 25
// 1471013: 35

// 23456:20
// 246810:30

// 34567:25
// 357911:35
