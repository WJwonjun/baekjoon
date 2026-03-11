#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int inorder[100000]; // left -> root -> right
int postorder[100000]; // left -> right -> root
int N;

void check(int inleft, int inright, int postleft, int postright){
	
	if (inleft > inright || postleft > postright) return;
	int target = postorder[postright];

	int* start = inorder+ inleft;
	int* end = inorder + inright + 1;
	int* it = std::find(start, end, target);
	int root = it - inorder;
	int leftsize = root - inleft;

	cout << inorder[root] << " ";

	check(inleft, root-1, postleft, postleft+leftsize-1);
	check(root+1, inright, postleft+leftsize, postright-1);
	return;
}

int main() {
	// 코드 작성

	cin >> N;
	for(int i=0;i<2;i++){
		for(int j=0;j<N;j++){
			if(i==0) cin >> inorder[j];
			else cin >> postorder[j];
		}
	}
	check(0, N-1,0,N-1);
// root -> left -> right
	
	return 0;
}