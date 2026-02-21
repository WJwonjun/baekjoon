#include <iostream>
#include <vector>
using namespace std;

struct point{
	int x,y;
	point(int _x, int _y): x(_x),y(_y){}
};

int ccw(point a, point b, point c) {
    int val = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    if (val > 0) return 1;   // 반시계
    if (val < 0) return -1;  // 시계
    return 0;                // 일직선
}

struct line{
	point p1,p2;
	int root;
	int cnt = 1;

	line(point a, point b, int num): p1(a), p2(b), root(num) {}

	bool isIntersect(line other) {
        int res1 = ccw(p1, p2, other.p1) * ccw(p1, p2, other.p2);
        int res2 = ccw(other.p1, other.p2, p1) * ccw(other.p1, other.p2, p2);

        if (res1 <= 0 && res2 <= 0) {
           
            if (res1 == 0 && res2 == 0) {

                pair<int, int> l1_x = {min(p1.x, p2.x), max(p1.x, p2.x)};
                pair<int, int> l1_y = {min(p1.y, p2.y), max(p1.y, p2.y)};
                pair<int, int> l2_x = {min(other.p1.x, other.p2.x), max(other.p1.x, other.p2.x)};
                pair<int, int> l2_y = {min(other.p1.y, other.p2.y), max(other.p1.y, other.p2.y)};

                return l1_x.first <= l2_x.second && l2_x.first <= l1_x.second &&
                       l1_y.first <= l2_y.second && l2_y.first <= l1_y.second;
            }
            return true; // 일반적인 교차 상황
        }
        return false; // 만나지 않음
    }
};


int main() {
	// 코드 작성
	int N;
	cin >> N;
	vector<line> linelist;

	for(int i=0;i<N;i++){
		int x1,y1,x2,y2;
		cin >> x1 >> y1 >> x2 >> y2;
		linelist.push_back(line(point(x1,y1),point(x2,y2),i));
		
		
		

	}


	cout << ans << endl;
	cout << max(cnt) << endl;
	return 0;
}