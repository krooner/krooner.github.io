#include <stdio.h>

int N, ret;
int map[100][100];

int main(){
    scanf("%d", &N);

    for (int i = 0; i<N; ++i){
        for (int j = 0; j<N; ++j){
            scanf("%d", &map[i][j]);
        }
    }

    ret = 0;

    printf("%d\n", ret);


    return 0;
}