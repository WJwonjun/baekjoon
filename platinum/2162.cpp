#include <iostream>
#include <vector>
#include <set>
using namespace std;

int parent[3001];
int cnt[3001];


struct Point {
    int x, y;
    // 좌표 비교를 위한 연산자 오버로딩 (일직선 겹침 확인용)
    bool operator<=(const Point& other) const {
        if (x == other.x) return y <= other.y;
        return x <= other.x;
    }
};


struct Line {
    Point p1, p2;
};

int find(int i){
	if(parent[i]==i) return i;
	return parent[i] = find(parent[i]);
}

void unite(int i, int j){
	int iroot = find(i);
	int jroot = find(j);
	if(iroot!=jroot){
		parent[iroot] = jroot;
		cnt[jroot] +=cnt[iroot];
	}
}

int ccw(Point a, Point b, Point c) {
    long long res = (a.x * b.y + b.x * c.y + c.x * a.y) - (b.x * a.y + c.x * b.y + a.x * c.y);
    if (res > 0) return 1;
    if (res < 0) return -1;
    return 0;
}

bool check(Point a, Point b, Point c, Point d) {
    int abc = ccw(a, b, c);
    int abd = ccw(a, b, d);
    int cda = ccw(c, d, a);
    int cdb = ccw(c, d, b);

    if (abc * abd == 0 && cda * cdb == 0) {
        // 선분의 방향을 작은 점 -> 큰 점 순으로 정렬
        if (b <= a) swap(a, b);
        if (d <= c) swap(c, d);
        
        // 겹침 판별
        return c <= b && a <= d;
    }
    return (long long)abc * abd <= 0 && (long long)cda * cdb <= 0;
}


int main() {
	// 코드 작성
	int N;
	vector<Line> linelist;

	cin >> N;

	for(int i=0;i<N;i++){
		cnt[i] = 1;
		parent[i] = i;
		int x1,y1,x2,y2;
		cin >> x1 >> y1 >> x2 >> y2;
		Point p1 = {x1,y1};
		Point p2 = {x2,y2};
		Line newline = {p1,p2};
		linelist.push_back(newline);
		for(int j=0;j<i;j++){
			if(check(linelist[j].p1,linelist[j].p2,newline.p1,newline.p2)){
				unite(j,i);
			}

		}
	}

	int group = 0, max_num = -1;
	for(int i=0;i<N;i++){
		if(parent[i]==i){
			group++;
			if(cnt[i]>max_num) max_num = cnt[i];
		}
		// cout << parent[i] << endl;
		// cout << cnt[i] << endl;
	}

	cout << group << endl;
	cout << max_num << endl;
	return 0;
}