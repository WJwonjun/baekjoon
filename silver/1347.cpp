#include <iostream>
#include <vector>
using namespace std;


int get_position(int origin, char turn){
    if(turn=='R'){
        if(origin==4) return 1;
        return ++origin;
    }
    else{
        if(origin==1) return 4;
        return --origin;
    }
}

int main(){
    int N;
    cin >> N;
    string records;
    cin >> records;

    int position = 4;
    // 1:왼 2:위 3:오 4:아래

    vector<vector<bool>> visited(100, vector<bool>(100,false));
    visited[50][50] = true;
    int max_x=50,max_y = 50,min_x = 50, min_y = 50, cur_x = 50, cur_y = 50;

    for(int i=0;i<N;i++){
        if(records[i]!='F'){
            position = get_position(position, records[i]);
        }
        else{
            switch (position){
                case 1:
                    if(--cur_x<min_x) min_x = cur_x;
                    visited[cur_y][cur_x]=true;
                    break;
                case 2:
                    if(--cur_y<min_y) min_y = cur_y;
                    visited[cur_y][cur_x]=true;
                    break;
                case 3:
                    if(++cur_x>max_x) max_x = cur_x;
                    visited[cur_y][cur_x]=true;
                    break;
                case 4:
                    if(++cur_y>max_y) max_y = cur_y;
                    visited[cur_y][cur_x]=true;
                    break;
            }
        }
    }
    for(int y = min_y; y <= max_y; y++){
    for(int x = min_x; x <= max_x; x++){
        cout << (visited[y][x] ? '.' : '#');
    }
    cout << '\n';
}

}