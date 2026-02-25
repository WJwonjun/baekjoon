#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int maps[21][21];
int ans = 0;
int N;

void moveup() {
    for (int x = 0; x < N; x++) {
        queue<int> q;
        // 1. 0이 아닌 숫자만 큐에 담기
        for (int y = 0; y < N; y++) {
            if (maps[y][x] != 0) {
                q.push(maps[y][x]);
                maps[y][x] = 0; // 원본은 일단 비움
            }
        }

        int target_y = 0;
        // 2. 큐에서 하나씩 꺼내어 합치기 처리
        while (!q.empty()) {
            int current = q.front();
            q.pop();

            // 다음 숫자와 같으면 합치기
            if (!q.empty() && q.front() == current) {
                maps[target_y++][x] = current * 2;
                q.pop();
            } else {
                maps[target_y++][x] = current;
            }
        }
    }
}

void movedown(){
    for (int x = 0; x < N; x++) {
        queue<int> q;
        // 1. 0이 아닌 숫자만 큐에 담기
        for (int y = N-1; y >=0; y--) {
            if (maps[y][x] != 0) {
                q.push(maps[y][x]);
                maps[y][x] = 0; // 원본은 일단 비움
            }
        }

        int target_y = N-1;
        // 2. 큐에서 하나씩 꺼내어 합치기 처리
        while (!q.empty()) {
            int current = q.front();
            q.pop();

            // 다음 숫자와 같으면 합치기
            if (!q.empty() && q.front() == current) {
                maps[target_y--][x] = current * 2;
                q.pop();
            } else {
                maps[target_y--][x] = current;
            }
        }
    }
}

void moveleft() {
    for (int y = 0; y < N; y++) {
        queue<int> q;
        // 1. 0이 아닌 숫자만 큐에 담기
        for (int x = 0; x < N; x++) {
            if (maps[y][x] != 0) {
                q.push(maps[y][x]);
                maps[y][x] = 0; // 원본은 일단 비움
            }
        }

        int target_x = 0;
        // 2. 큐에서 하나씩 꺼내어 합치기 처리
        while (!q.empty()) {
            int current = q.front();
            q.pop();

            // 다음 숫자와 같으면 합치기
            if (!q.empty() && q.front() == current) {
                maps[y][target_x++] = current * 2;
                q.pop();
            } else {
                maps[y][target_x++] = current;
            }
        }
    }
}

void moveright(){
    for (int y = 0; y < N; y++) {
        queue<int> q;
        // 1. 0이 아닌 숫자만 큐에 담기
        for (int x = N-1; x >=0; x--) {
            if (maps[y][x] != 0) {
                q.push(maps[y][x]);
                maps[y][x] = 0; // 원본은 일단 비움
            }
        }

        int target_x = N-1;
        // 2. 큐에서 하나씩 꺼내어 합치기 처리
        while (!q.empty()) {
            int current = q.front();
            q.pop();

            // 다음 숫자와 같으면 합치기
            if (!q.empty() && q.front() == current) {
                maps[y][target_x--] = current * 2;
                q.pop();
            } else {
                maps[y][target_x--] = current;
            }
        }
    }
}


void process(int cnt){
    if(cnt==5){
        int max_num = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (maps[i][j] > max_num) max_num = maps[i][j];
            }
        }
        ans = max(max_num, ans);
        return;
    }
    int temp_maps[21][21];
    memcpy(temp_maps, maps, sizeof(maps));

    moveup();
    process(cnt+1);
    memcpy(maps,temp_maps,sizeof(maps));

    movedown();
    process(cnt+1);
    memcpy(maps,temp_maps,sizeof(maps));

    moveleft();
    process(cnt+1);
    memcpy(maps,temp_maps,sizeof(maps));

    moveright();
    process(cnt+1);
    memcpy(maps,temp_maps,sizeof(maps));

}

int main() {
	// 코드 작성
    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> maps[i][j];
        }
    }
    process(0);
    

    cout << ans << endl;

	return 0;
}