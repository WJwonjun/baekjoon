#include <stdio.h>

void merge(long long int list[], long long int sorted[], int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    int k = left;

    // Merge two sorted halves into sorted[]
    while (i <= mid && j <= right) {
        if (list[i] <= list[j])
            sorted[k++] = list[i++];
        else
            sorted[k++] = list[j++];
    }

    // Copy remaining elements of the left half
    while (i <= mid) {
        sorted[k++] = list[i++];
    }

    while (j <= right) {
        sorted[k++] = list[j++];
    }

    for (i = left; i <= right; i++) {
        list[i] = sorted[i];
    }
}

void merge_sort(long long int list[], long long int sorted[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;  // 중간 위치를 계산하여 리스트를 균등 분할 - 분할(Divide)
        merge_sort(list, sorted, left, mid);      
        merge_sort(list, sorted, mid + 1, right); 
        merge(list, sorted, left, mid, right);    // 정렬된 2개의 부분 배열을 합병 - 결합(Combine)
    }
}

int main() {
    int N;
    scanf("%d", &N);

    long long int nums[N];
    long long int sorted[N];

    for (int i = 0; i < N; i++) {
        long long int a, b;
        scanf("%lld %lld", &a, &b);
        nums[i] = b - a;
    }

    // sort nums
    if (N > 1) {
        merge_sort(nums, sorted, 0, N - 1);
    }

    if (N % 2 == 0) {
        printf("%lld", (nums[N/2] - nums[N/2 - 1] + 1));
    } else {
        printf("1");
    }

    return 0;
}
