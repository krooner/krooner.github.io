#include <iostream>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int ccw[] = {2, 0, 3, 1};
int cw[] = {2, 1, 3, 0};

int room[51][51] = {0,};

int r, c, t;
int ur, uc, dr, dc;

int ddr[] = {-1, 1, 0, 0};
int ddc[] = {0, 0, 1, -1};


void solve() {

    for (int sec = 0; sec < t; ++sec) {

        queue <pair <int, int> > q;

        for (int i =0; i<r; ++i) {
            for (int j= 0; j<c; ++j) {
                if (room[i][j]>=1) {
                    q.push({i,j});
                }
            }
        }

        int copy[51][51] = {0, };

        for (int i =0; i<r; ++i) {
            for (int j= 0; j<c; ++j) {
                copy[i][j] = room[i][j];
            }
        }

        while (!q.empty()) {

            int nr = q.front().first;
            int nc = q.front().second;

            q.pop();

            int temp = copy[nr][nc] / 5;

            for (int i = 0; i<4; ++i) {
                int next_r = nr + ddr[i];
                int next_c = nc + ddc[i];

                if (0<= next_r && next_r <r && 0<= next_c && next_c <c) {
                    if (copy[next_r][next_c] >= 0) {
                        room[next_r][next_c] += temp;
                        room[nr][nc] -= temp;
                    }
                }
            }

        }

        for (int i =0; i<r; ++i) {
            for (int j= 0; j<c; ++j) {
                copy[i][j] = room[i][j];
            }
        }

        int ar = ur;
        int ac = uc + 1;

        room[ar][ac] = 0;

        for (int i=0; i<4; i++) {
            while (1) {
                int nextr = ar + ddr[ccw[i]];
                int nextc = ac + ddc[ccw[i]];

                if (nextr == ur && nextc == uc)
					break;
				if (!(0 <= nextr && nextr < r && 0 <= nextc && nextc < c))
					break;

				room[nextr][nextc] = copy[ar][ac];
				ar = nextr;
				ac = nextc;
            }

        }

        ar = dr;
		ac = dc + 1;
		room[ar][ac] = 0;
		for (int i = 0; i < 4; i++)
		{
			while (1)
			{
				int nextr = ar + ddr[cw[i]];
				int nextc = ac + ddc[cw[i]];

				if (nextr == dr && nextc == dc)
					break;
				if (!(0 <= nextr && nextr < r && 0 <= nextc && nextc < c))
					break;

				room[nextr][nextc] = copy[ar][ac];
				ar = nextr;
				ac = nextc;
			}
		}

        


    }


}




int main() {

    ur = -1; uc = -1;


    cin>>r>>c>>t;

    for (int i=0; i<r; ++i) {
        for (int j=0; j<c; ++j) {
            cin>>room[i][j];

            if (ur == -1 && uc == -1 && room[i][j] == -1) {
                ur = i; uc = j;
            }

            if (ur != -1 && uc != -1 && room[i][j] == -1) {
                dr = i; dc = j;
            }
        }
    }

    solve();

    int sum = 0;

    for (int i=0; i<r; ++i) {
        for (int j = 0; j<c; ++j) {
            if (room[i][j]>=1) {
                sum += room[i][j];
            }
        }
    }

    cout<<sum<<endl;

    return 0;
}