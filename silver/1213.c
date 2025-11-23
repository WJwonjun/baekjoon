#include <stdio.h>
#include <string.h>

int main(){
    int ch[26]={0};
    
    char c;
    while(scanf("%c",&c)==1){
        ch[c-'A']++;
    }
    int cnt=0;
    for(int i=0;i<26;i++){
        if(ch[i]%2==1) cnt++;
    }
    if(cnt>1){
        printf("I'm Sorry Hansoo");
        return 0;
    }
    else if(cnt==0){
        char ans[50];
        int len = 0;

        for(int i=0;i<26;i++){
            for(int j=0;j<(ch[i]/2);j++){
                ans[len++] = i+'A';
            }
        }
        int half = len;
        half--;
        while(half>=0){ ans[len++] =ans[half--]; } 
        ans[len] = '\0';

        printf("%s",ans);
    }
    else{
        char ans[50];
        int len = 0;
        int special;
        for(int i=0;i<26;i++){
            for(int j=0;j<(ch[i]/2);j++){
                ans[len++] = i+'A';            
            }
            if(ch[i]%2==1) special=i;
        }
        int half = len-1;
        ans[len++] = special+'A';
        while(half>=0){ans[len++] =ans[half--];}
        ans[len] = '\0';
        printf("%s",ans);
        

    }
    
}