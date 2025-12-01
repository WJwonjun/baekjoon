#include <stdio.h>
#include <math.h>
int main(){
    int N;
    scanf("%d",&N);
    double X[N],Y[N];
    double tmp,ans = 0;
    for (int i=0;i<N;i++){
        scanf("%lf %lf",&X[i],&Y[i]);
    }

    for (int i=0;i<N;i++){
        for (int j=i+1;j<N;j++){
            for (int k=j+1;k<N;k++){
                tmp = fabs(((X[i]*Y[j]+X[j]*Y[k]+X[k]*Y[i]) - (X[j]*Y[i]+X[k]*Y[j]+X[i]*Y[k])))*(0.5);
                if (tmp > ans) ans = tmp;
                
            }
        }
    }
    printf("%f",ans);
}