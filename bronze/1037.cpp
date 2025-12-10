#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int N;
    std::cin >> N;

    std::vector<int> nums(N);
    for(int i = 0; i < N; i++) {
        std::cin >> nums[i];
    }
    if(N==1) std::cout << nums[0]*nums[0];
    else{
    int minVal = *std::min_element(nums.begin(), nums.end());
    int maxVal = *std::max_element(nums.begin(), nums.end());

    std::cout << minVal * maxVal;
    }
}
