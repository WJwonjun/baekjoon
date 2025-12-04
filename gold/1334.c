#include <stdio.h>
#include <string.h>

void increment_mid(char* s, int len) {
    int mid = (len - 1) / 2;
    int left = mid;
    int right = (len % 2 == 0) ? mid + 1 : mid; // 짝수면 left+1, 홀수면 left와 같음

    right = len - 1 - left;

    while (left >= 0) {
        if (s[left] == '9') {
            s[left] = '0';
            s[right] = '0';
            left--;
            right++;
        } else {
            s[left]++;
            s[right] = s[left];
            break;
        }
    }
}

int main() {
    char num[100]; // 넉넉한 크기
    scanf("%s", num);

    int len = strlen(num);

    // 1. 입력값에 1을 더함 (입력값보다 '큰' 수를 찾아야 하므로)
    int temp = len - 1;
    while (temp >= 0) {
        if (num[temp] == '9') {
            num[temp] = '0';
            temp--;
        } else {
            num[temp]++;
            break;
        }
    }

    // "99" -> "100" 처럼 자릿수가 늘어난 경우 처리
    if (temp < 0) {
        char buffer[100];
        strcpy(buffer, num);
        num[0] = '1';
        strcpy(num + 1, buffer);
        len++;
        num[len] = '\0';
    }

    // 2. 일단 왼쪽 절반을 오른쪽에 복사해서 팰린드롬 생성
    char candidate[100];
    strcpy(candidate, num);
    
    for (int i = 0; i < len / 2; i++) {
        candidate[len - 1 - i] = candidate[i];
    }

    // 3. 만든 팰린드롬이 (입력+1)보다 크거나 같으면 정답
    // 작다면 가운데 숫자를 증가시켜서 다시 맞춤
    if (strcmp(candidate, num) >= 0) {
        printf("%s", candidate);
    } else {
        increment_mid(candidate, len);
        printf("%s", candidate);
    }

    return 0;
}