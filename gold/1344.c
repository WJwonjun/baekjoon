#include <stdio.h>
#include <math.h>

int comb(int a, int b){
    long long int c=1;
    for(int i=a;i>b;i--){
        c*=i;
    }
    for(int i=1;i<=(a-b);i++){
        c/=i;
    }
    return c;

}
int prime(int a){
    if (a==2 || a==3 || a==5 || a==7 || a==11|| a==13||a==17) return 1;
    else return 0;
}
int main(){
    double a,b;
    scanf("%lf\n%lf",&a,&b);
    a/=100;
    b/=100;
    // 2,3,5,7,11,13,17
    double a_res=0, b_res=0;
    for(int i=0;i<18;i++){
        if(prime(i)==0) continue;
        a_res+=comb(18,i)*pow(a,i)*pow(1-a,18-i);
        b_res+=comb(18,i)*pow(b,i)*pow(1-b,18-i);
    }
    printf("%f",1-(1-a_res)*(1-b_res));

    

}