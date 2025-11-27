    #include <stdio.h>
    #include <stdbool.h>
    #define max(x, y) ((x) > (y) ? (x) : (y))

    int main(){
        int N;
        scanf("%d",&N);
        char friends[50][50];
        int max_num=0;
        for(int i=0;i<N;i++){
            scanf("%s",friends[i]);
        }

        for(int i=0;i<N;i++){
            bool check[N];
            for (int t = 0; t < N; t++)
                check[t] = false;

            for(int j=0;j<N;j++){
                if (friends[i][j]=='Y') check[j]=true;
            }

            for(int j = 0; j < N; j++){
            if (friends[i][j] == 'Y') {
                for(int k = 0; k < N; k++){
                    if (friends[j][k] == 'Y')
                        check[k] = true;
                }
            }
        }

            check[i] = false;
            
            int cnt = 0;
            for(int x=0;x<N;x++){
                if( check[x]==true){ 
                    cnt++; }
                
            }


        
            max_num = max(max_num, cnt);
        }
        printf("%d",max_num);
    }

