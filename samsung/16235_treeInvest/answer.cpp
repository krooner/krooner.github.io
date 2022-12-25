// #include <stdio.h>
#include <iostream>
#include <vector> // vectoor is from the std namespace, so you must use std!  https://stackoverflow.com/questions/16704090/vector-is-not-a-template
#include <algorithm> // sort

using namespace std;

const int dy[] = {0, 0, 1, -1, -1, 1, 1, -1};
const int dx[] = {1, -1, 0, 0, 1, 1, -1, -1};

int n, m, k;

int array[10][10];
int cur[10][10];
int death[10][10];

vector<int> tree [10][10];

void spring() {
    for (int i = 0; i<n; ++i) {
        for (int j = 0; j<n; ++j) {

            sort(tree[i][j].begin(), tree[i][j].end());

            vector<int> tmp;

            for (int age: tree[i][j]) {
                if (age > cur[i][j]) {
                    death[i][j] += age/2;
                } else {
                    tmp.push_back(age +1);
                    cur[i][j] -= age;
                }
            }

            swap(tree[i][j], tmp);

        }
    }
}

void summer() {
    for (int i = 0; i<n; ++i) {
        for (int j = 0; j<n; ++j) {
            cur[i][j] += death[i][j];
            death[i][j] = 0;
        }
    }
}

void fall() {
    for (int i = 0;  i<n; ++i) {
        for (int j = 0; j<n; ++j ) {
            
            for (int age: tree[i][j]) {
                if (age ==1 ) {
                    break;
                }
                if (age%5 != 0) {
                    continue;
                }

                for (int k = 8; k--;) {
                    int ny = i + dy[k];
                    int nx = j + dx[k];

                    if (nx<0 || nx>=n || ny<0 || ny>=n ) {
                        continue;
                    }

                    tree[ny][nx].push_back(1);
                }
            }
        }
    }
}

void winter() {

    for (int i =0; i<n; ++i) {
        for ( int j = 0; j<n; ++j) {
            cur[i][j] += array[i][j];
        }
    }
}

int main() {

    // scanf("%d %d %d", &n, &m, &k);
    cin>>n>>m>>k;

    for (int i = 0; i<n; ++i) {
        for (int j = 0; j<n; ++j) {
            // scanf("%d", &array[i][j]);
            cin>>array[i][j];
            cur[i][j] = 5;
        }
    }

    while (m--) {

        int y, x, z;
        // scanf("%d %d %d", &y, &x, &z);
        cin>>y>>x>>z;
        --x, --y;
        tree[y][x].push_back(z);
    }

    while (k--) {
        spring();
        summer();
        fall();
        winter();
    }

    int ans = 0;
    for (int i = 0; i<n; ++i) {
        for (int j = 0; j<n; ++j) {
            ans += tree[i][j].size();
        }
    }

    cout<<ans;


    return 0;
}

