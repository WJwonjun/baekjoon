#include <stdio.h>
#include <string.h>

void reverse(char *s) {
    int n = strlen(s);
    for(int i=0; i<n/2; i++) {
        char tmp = s[i];
        s[i] = s[n-1-i];
        s[n-1-i] = tmp;
    }
}

int main() {
    char word[51], ans[51];
    for(int k=0;k<50;k++) ans[k]='z';
    ans[50]='\0';

    scanf("%s", word);
    int len = strlen(word);

    char a[51], b[51], c[51], nword[51];

    for(int i=1; i < len; i++) {
        for(int j=i+1; j < len; j++) {
            nword[0] = '\0';

            strncpy(a, word, i);
            a[i] = '\0';
            strncpy(b, word+i, j-i);
            b[j-i] = '\0';
            strcpy(c, word+j);

            reverse(a);
            reverse(b);
            reverse(c);

            strcat(nword, a);
            strcat(nword, b);
            strcat(nword, c);

            if(strcmp(nword, ans) < 0) {
                strcpy(ans, nword);
            }
        }
    }

    printf("%s\n", ans);
}
