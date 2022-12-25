#include <stdio.h>

int N, K;
int A[200];

int solve() {

    int ret = 0;
    int zero_count = 0;

    int robot[200*1000]; // 각 element는 robot이 위치한 컨베이어 벨트
    int front = 0, back = 0;


    // 
    while (zero_count<K) {
        ++ret;

        // 컨베이어 벨트를 한 칸씩 이동시킴 - 각 칸의 내구도를 한칸씩 전진하여 옮김
        int temp = A[2*N-1];
        for (int i = 2*N - 1; i >= 1; --i) {
            A[i] = A[i-1];
        }
        A[0] = temp;

        for (int i = front; i <back; ++i) {
            ++robot[i];

            if (robot[i] == N-1) { // 로봇이 내리는 위치에 있는 경우 - robot array에서, 작은 Index일수록 먼저 컨베이어 벨트에 들어온 로봇일 것. - 그렇기 때문에 ++front의 의미는 (현재 컨베이어벨트 앞부분에서) 가장 오래 있었던 로봇을 내리는 것을 의미
                ++front;
            }
        }

        for (int i = front; i < back; ++i) {
            int next = robot[i] + 1; // i robot이 위치한 칸보다 한 칸 전진된 칸
            if (A[next] == 0 || (i != front && robot[i-1] == next)) { // 그 칸의 내구도가 0이거나 i robot이 처음 놓여진 것이 아닌 상황에서 i 직전에 놓인 (i-1) robot이 "i" robot 바로 앞에 있는 경우 - Pass
                continue;
            }

            robot[i] = next; // 다음 칸의 내구도가 0보다 크고 로봇도 없기 때문에 i robot은 다음 칸으로 이동
            if (next == N-1) { // 이동했는데 내리는 위치면 OUT
                ++front;
            }
            --A[next]; // 로봇이 옮겨왔으니 해당 칸의 내구도 -1
            if (A[next] == 0) { // 그런데 해당 칸의 내구도가 0이 되었다면 카운팅
                ++zero_count;
            }
        }

        if (A[0]>0 && (back == 0 || robot[back-1] != 0)) { // 올리는 위치의 내구도가 0 이상이면서, 처음 올리는 경우이거나 가장 최근에 올린 로봇이 올리는 위치에 없는 경우
            robot[back++] = 0; // 로봇을 올리는 위치에 새로 올림
            --A[0]; // 올리는 위치에 있는 칸 내구도 1 감소

            if (A[0] == 0 ) { // 그런데 내구도 0 되면 카운팅
                ++zero_count;
            }
        }
    }

    return ret;

}


int main(){

    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; ++i) {
        scanf("%d %d", &A[i*2], &A[i*2+1]);
    }

    int ret = solve();

    printf("%d\n", ret);

    return 0;
}