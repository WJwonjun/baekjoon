#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

bool isPal(const string& s, int start){
    int l = start, r = s.size()-1;
    while (l < r) {
        if (s[l++] != s[r--]) return false;
    }
    return true;
}

int main(){
    string s;
    cin >> s;
    int n = s.size();

    for(int i=0;i<n;i++){
        if(isPal(s,i)){
            cout << n+i << endl;
            break;
        }
    }
}