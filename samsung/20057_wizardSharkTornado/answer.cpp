#include <stdio.h>

int N;
int map[500][500];

const int dy[] = { 0, +1, 0, -1 };
const int dx[] = { -1, 0, 1, 0};


int main(){

    scanf("%d", &N);

    for (int i=0; i<N; ++i){
        for (int j=0; j<N; ++j) {
            scanf("%d", &map[i][j]);
        }
    }

    int start_x, start_y;
    start_x = int(N/2); start_y = int(N/2);
    int curr_x, curr_y;
    curr_x = start_x; curr_y = start_y;

    int index = 0;

    for (int i=0; i<2*N-1;++i) {
        index = index % 4;

        int direct = 

    }




    return 0;
}