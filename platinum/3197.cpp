#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

char maps[1500][1500];
bool w_visited[1500][1500];
bool l_visited[1500][1500];

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int R,C;
	cin >> R >> C;
	queue<pair<int,int>> QL1,QL2,QW1,QW2;

	for (int i = 0; i < R; i++) {
		string row;
		cin >> row; 
		
		for (int j = 0; j < C; j++) {
			maps[i][j] = row[j]; 

			if(row[j]=='L' && QL1.empty()){
				QL1.emplace(i,j);
				QW1.emplace(i,j);
				l_visited[i][j] = true;
				w_visited[i][j] = true;
			}else if(row[j]=='.' || row[j]=='L'){
				QW1.emplace(i,j);
				w_visited[i][j]  = true;
				l_visited[i][j]  = false;
			}else {
				l_visited[i][j] = false;
				w_visited[i][j] = false;
			}
		}
	}
	
	int cnt = 0;
	int dayswitch = 0;
	while(true){
		if(dayswitch==0){
			//cout << "QL1" << endl;
			while(!QL1.empty()){
				auto [y,x] = QL1.front();
				QL1.pop();
				//cout << y << x << endl;
				for(int i=0;i<4;i++){
					int ny = y + dy[i];
					int nx = x + dx[i];
					if(0<=ny && ny < R && 0<=nx && nx<C){
						if(l_visited[ny][nx]==false){
							if(maps[ny][nx]=='.'){
								QL1.emplace(ny,nx);
							}else if(maps[ny][nx]=='X'){
								QL2.emplace(ny,nx);
							}else{ // 'L' case
								cout << cnt << endl;
								return 0;
							}
							l_visited[ny][nx] = true;
						}
					}
				}
			}
			//cout << "QW1" << endl;
			while(!QW1.empty()){
				auto [y,x] = QW1.front();
				QW1.pop();
				//cout << y << x << endl;
				for(int i=0;i<4;i++){
				int ny = y + dy[i];
				int nx = x + dx[i];
				if(0<=ny && ny < R && 0<=nx && nx<C){
					if(w_visited[ny][nx]==false){
						if(maps[ny][nx]=='X'){
							QW2.emplace(ny,nx);
							maps[ny][nx] = '.';
						}
						w_visited[ny][nx] = true;
					}
				}
			}
		}
		
			
			dayswitch++;
		}
		else{
			//cout << "QL2" << endl;
			while(!QL2.empty()){
				auto [y,x] = QL2.front();
				QL2.pop();
				//cout << y << x << endl;
				for(int i=0;i<4;i++){
					int ny = y + dy[i];
					int nx = x + dx[i];
					if(0<=ny && ny < R && 0<=nx && nx<C){
						if(l_visited[ny][nx]==false){
							if(maps[ny][nx]=='.'){
								QL2.emplace(ny,nx);
							}else if(maps[ny][nx]=='X'){
								QL1.emplace(ny,nx);
							}else{ // 'L' case
								cout << cnt << endl;
								return 0;
							}
							l_visited[ny][nx] = true;
						}
					}
				}
			}
			//cout << "QW2" << endl;
			while(!QW2.empty()){
				auto [y,x] = QW2.front();
				QW2.pop();
				//cout << y << x << endl;
				for(int i=0;i<4;i++){
				int ny = y + dy[i];
				int nx = x + dx[i];
				if(0<=ny && ny < R && 0<=nx && nx<C){
					if(w_visited[ny][nx]==false){
						if(maps[ny][nx]=='X'){
							maps[ny][nx] = '.';
							QW1.emplace(ny,nx);
						}
						w_visited[ny][nx] = true;
					}
				}
			}
		}
		
			
			dayswitch--;
		}

		cnt++;
	}
	
	return 0;
}