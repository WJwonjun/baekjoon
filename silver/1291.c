//1 : 123 합 가능 + 각 자릿수 합이 홀수
//2: 2/4 or 소인수 개수 짝수
//3: 둘다 아님
//4: 둘다임


#include <stdio.h>
int main(){
    int one=0, two=0;
    int num;
    scanf("%d",&num);
    int tmp = num;
    int cal = 0;
    while(tmp>0){
        cal+=tmp%10;
        tmp/=10;
    }
    if (num>5 && (cal%2==1)){
        one = 1;
    }

    int cnt = 0;
    tmp = num;
    for(int i=2;i<=num;i++){
        int flag = 0;
        if(tmp==1) break;
        while (tmp%i==0){
            tmp/=i;
            flag = 1;
        }
        if (flag==1) cnt++;
    }
    if (num==2 || num==4 || ((cnt%2==0)&& (cnt>=2))) two = 1;

    if (one && two){
        printf("%c",'4');
    }
    else if(one){
        printf("%c",'1');
    }
    else if(two){
        printf("%c",'2');
    }
    else printf("%c",'3');



}