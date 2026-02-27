#include <iostream>
#include <string>
#include <cstring>
#include <queue>
using namespace std;

int maps[11][11];
int R_Y,R_X,B_Y,B_X;
int R,C;
int ans = 11;

void moveleft(){
	int redfirst = -1;
	if(R_Y==B_Y){
		if(R_X<B_X) redfirst = 1;
		else redfirst = 0;
	}
	int nextX = 0;
	if(redfirst==0){ // 파 .. 빨 ..
		for(int x=0;x<C;x++){
			if(maps[R_Y][x]=='#'){
				nextX = x+1;
			}else if(maps[R_Y][x]=='O'){
				nextX = x;
			}else if(x==B_X){
				B_X = nextX;
				if(maps[B_Y][nextX]!='O') nextX++;
			}else if(x==R_X){
				R_X = nextX;
			}
		}
	}
	else if(redfirst==1) { // 빨 .. 파 ..
		for(int x=0;x<C;x++){
			if(maps[B_Y][x]=='#'){
				nextX = x+1;
			}else if(maps[B_Y][x]=='O'){
				nextX = x;
			}else if(x==R_X){
				R_X = nextX;
				if(maps[R_Y][nextX]!='O') nextX++;
			}else if(x==B_X){
				B_X = nextX;
			}
		}
	}
	else { // 안겹치는 경우
		for(int x=0;x<C;x++){
			if(maps[B_Y][x]=='#'){
				nextX = x+1;
			}else if(maps[B_Y][x]=='O'){
				nextX = x;
			}else if(x==B_X){
				B_X = nextX;
				break;
			}
		}
		int nextX = 0;
		for(int x=0;x<C;x++){
			if(maps[R_Y][x]=='#'){
				nextX = x+1;
			}else if(maps[R_Y][x]=='O'){
				nextX = x;
			}else if(x==R_X){
				R_X = nextX;
				break;
			}
		}
	}
}

void moveright(){
	int redfirst = -1;
	if(R_Y==B_Y){
		if(R_X>B_X) redfirst = 1;
		else redfirst = 0;
	}
	int nextX = C-1;
	if(redfirst==0){ // 빨 .. 파 ..
		for(int x=C-1;x>=0;x--){
			if(maps[R_Y][x]=='#'){
				nextX = x-1;
			}else if(maps[R_Y][x]=='O'){
				nextX = x;
			}else if(x==B_X){
				B_X = nextX;
				if(maps[B_Y][nextX]!='O') nextX--;
			}else if(x==R_X){
				R_X = nextX;
			}
		}
	}
	else if(redfirst==1) { // 파 .. 빨 ..
		for(int x=C-1;x>=0;x--){
			if(maps[B_Y][x]=='#'){
				nextX = x-1;
			}else if(maps[B_Y][x]=='O'){
				nextX = x;
			}else if(x==R_X){
				R_X = nextX;
				if(maps[R_Y][nextX]!='O') nextX--;
			}else if(x==B_X){
				B_X = nextX;
			}
		}
	}
	else { // 안겹치는 경우
		for(int x=C-1;x>=0;x--){
			if(maps[B_Y][x]=='#'){
				nextX = x-1;
			}else if(maps[B_Y][x]=='O'){
				nextX = x;
			}else if(x==B_X){
				B_X = nextX;
				break;
			}
		}
		int nextX = C-1;
		for(int x=C-1;x>=0;x--){
			if(maps[R_Y][x]=='#'){
				nextX = x-1;
			}else if(maps[R_Y][x]=='O'){
				nextX = x;
			}else if(x==R_X){
				R_X = nextX;
				break;
			}
		}
	}

}

void moveup(){
	int redfirst = -1;
	if(R_X==B_X){
		if(R_Y<B_Y) redfirst = 1;
		else redfirst = 0;
	}
	int nextY = 0;
	if(redfirst==0){ // 파 .. 빨 ..
		for(int y=0;y<R;y++){
			if(maps[y][R_X]=='#'){
				nextY = y+1;
			}else if(maps[y][R_X]=='O'){
				nextY = y;
			}else if(y==B_Y){
				B_Y = nextY;
				if(maps[nextY][B_X]!='O') nextY++;
			}else if(y==R_Y){
				R_Y = nextY;
			}
		}
	}
	else if(redfirst==1) { // 빨 .. 파 ..
		for(int y=0;y<R;y++){
			if(maps[y][B_X]=='#'){
				nextY = y+1;
			}else if(maps[y][B_X]=='O'){
				nextY = y;
			}else if(y==R_Y){
				R_Y = nextY;
				if(maps[nextY][R_X]!='O') nextY++;
			}else if(y==B_Y){
				B_Y = nextY;
			}
		}
	}
	else { // 안겹치는 경우
		for(int y=0;y<R;y++){
			if(maps[y][B_X]=='#'){
				nextY = y+1;
			}else if(maps[y][B_X]=='O'){
				nextY = y;
			}else if(y==B_Y){
				B_Y = nextY;
				break;
			}
		}
		int nextY = 0;
		for(int y=0;y<R;y++){
			if(maps[y][R_X]=='#'){
				nextY = y+1;
			}else if(maps[y][R_X]=='O'){
				nextY = y;
			}else if(y==R_Y){
				R_Y = nextY;
				break;
			}
		}
	}
}

void movedown(){
	int redfirst = -1;
	if(R_X==B_X){
		if(R_Y>B_Y) redfirst = 1;
		else redfirst = 0;
	}
	int nextY = R-1;
	if(redfirst==0){ // 파 .. 빨 ..
		for(int y=R-1;y>=0;y--){
			if(maps[y][R_X]=='#'){
				nextY = y-1;
			}else if(maps[y][R_X]=='O'){
				nextY = y;
			}else if(y==B_Y){
				B_Y = nextY;
				if(maps[nextY][B_X]!='O') nextY--;
			}else if(y==R_Y){
				R_Y = nextY;
			}
		}
	}
	else if(redfirst==1) { // 빨 .. 파 ..
		for(int y=R-1;y>=0;y--){
			if(maps[y][R_X]=='#'){
				nextY = y-1;
			}else if(maps[y][R_X]=='O'){
				nextY = y;
			}else if(y==R_Y){
				R_Y = nextY;
				if(maps[nextY][R_X]!='O') nextY--;
			}else if(y==B_Y){
				B_Y = nextY;
			}
		}
	}
	else { // 안겹치는 경우
		for(int y=R-1;y>=0;y--){
			if(maps[y][B_X]=='#'){
				nextY = y-1;
			}else if(maps[y][B_X]=='O'){
				nextY = y;
			}else if(y==B_Y){
				B_Y = nextY;
				break;
			}
		}
		int nextY = R-1;
		for(int y=R-1;y>=0;y--){
			if(maps[y][R_X]=='#'){
				nextY = y-1;
			}else if(maps[y][R_X]=='O'){
				nextY = y;
			}else if(y==R_Y){
				R_Y = nextY;
				break;
			}
		}
	}
}

void process(int cnt){
	if((maps[B_Y][B_X]=='O') || cnt>10 ){
		return;
	}
	if(maps[R_Y][R_X]=='O' && cnt<ans){
		ans = cnt;
		return;
	}

	int temp_R_Y = R_Y, temp_R_X = R_X, temp_B_Y = B_Y, temp_B_X = B_X;

	moveleft();
	process(cnt+1);
	R_Y = temp_R_Y; R_X = temp_R_X; B_Y = temp_B_Y; B_X = temp_B_X;
	
	moveright();
	process(cnt+1);
	//if(cnt==0) cout << R_X << " " << B_X << endl;
	R_Y = temp_R_Y; R_X = temp_R_X; B_Y = temp_B_Y; B_X = temp_B_X;
	

	moveup();
	process(cnt+1);
	R_Y = temp_R_Y; R_X = temp_R_X; B_Y = temp_B_Y; B_X = temp_B_X;

	movedown();
	process(cnt+1);
	R_Y = temp_R_Y; R_X = temp_R_X; B_Y = temp_B_Y; B_X = temp_B_X;

}

int main() {
	// 코드 작성
	cin >> R >> C;

	for(int i=0;i<R;i++){
		string temp;
		cin >> temp;
		for(int j=0;j<C;j++){	
			if(temp[j]=='B'){
				B_Y = i;
				B_X = j;
				maps[i][j] = '.';
			}else if(temp[j]=='R'){
				R_Y = i;
				R_X = j;
				maps[i][j] = '.';	
			}else maps[i][j] = temp[j];
		}
	}

	process(0);
	if(ans==11) ans = -1;
	cout << ans << endl;
	
	return 0;
}