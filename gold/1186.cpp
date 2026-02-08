#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct rectangle {
    int num, x1, y1, x2, y2;
    rectangle(int _num, int _x1, int _y1, int _x2, int _y2)
        : num(_num), x1(_x1), y1(_y1), x2(_x2), y2(_y2) {}
};

struct Result {
    int num;
    long long visible_area;
};

int main(){
	int N, K;
	cin >> N >> K;

	vector<rectangle> reclist;
	vector<int> xs,ys;

	for (int i = 0; i < N; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        reclist.emplace_back(i, x1, y1, x2, y2);
        xs.push_back(x1); xs.push_back(x2);
        ys.push_back(y1); ys.push_back(y2);
    }


	sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());

	vector<int> visible_area(N,0);

	for (int i = 0; i < (int)xs.size() - 1; i++) {
        for (int j = 0; j < (int)ys.size() - 1; j++) {
			int cx1 = xs[i], cx2 = xs[i+1];
            int cy1 = ys[j], cy2 = ys[j+1];
            int cell_area = (cx2 - cx1) * (cy2 - cy1);
			
			for (int k = N - 1; k >= 0; k--) {
                if (reclist[k].x1 <= cx1 && cx2 <= reclist[k].x2 &&
                    reclist[k].y1 <= cy1 && cy2 <= reclist[k].y2) {
                    
                    visible_area[reclist[k].num] += cell_area;
                    break; 
		}
	}
}
}

	vector<Result> final_results;
    for (int i = 0; i < N; i++) {
        final_results.push_back({i, visible_area[i]});
    }

    sort(final_results.begin(), final_results.end(), [](const Result& a, const Result& b) {
        if (a.visible_area != b.visible_area) {
            return a.visible_area > b.visible_area; // 면적 내림차순
        }
        return a.num < b.num; // 번호 오름차순
    });

  
    vector<int> topK_nums;
    for (int i = 0; i < K && i < N; i++) {
        topK_nums.push_back(final_results[i].num);
    }

    
    sort(topK_nums.begin(), topK_nums.end());

    for (int i = 0; i < topK_nums.size(); i++) {

        cout << topK_nums[i]+1 << (i == topK_nums.size() - 1 ? "" : " ");
    }
    cout << endl;
}
