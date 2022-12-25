#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
 
using namespace std;
 
int a[20][20];
int dist[20][20];
int b_x, b_y;
int d;
int n;
int s_size = 2;
 
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
 
vector<pair<int, int> > eat;
pair<int, int> Min;

void initialize(){
    d = 987654321;
    eat.clear();
    memset(dist, 0, sizeof(dist));
}
 
void bfs(int s_x, int s_y) {
    queue<pair<int, int> > q;
    q.push(make_pair(s_x, s_y));
 
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
 
        for (int i = 0; i < 4; i++) {
            int mx = x + dx[i];
            int my = y + dy[i];
 
            if (0 <= mx && mx < n && 0 <= my && my < n) {
                if (dist[mx][my] == 0 && s_size >= a[mx][my]) {
                    dist[mx][my] = dist[x][y] + 1;
                    if (0 < a[mx][my] && a[mx][my] < s_size) {
                        if (d >= dist[mx][my]) {
                            eat.push_back(make_pair(mx, my));
                            d = dist[mx][my];
                            Min.first = mx;
                            Min.second = my;
                        }
                    }
                    q.push(make_pair(mx, my));
                }
            }
        }
    }
}
 
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
 
            if (a[i][j] == 9) { //아기상어 위치
                a[i][j] = 0;
                b_x = i;
                b_y = j;
            }
        }
    }
 
    int ans = 0;
    int cnt = 0;
 
    while (true) {
        
        initialize();
        bfs(b_x, b_y);
 
        if (eat.empty()) break;
        else {
            if (eat.size() == 1) {
                b_x = Min.first;
                b_y = Min.second;
            }
            else {            
                for (int i = 0; i < eat.size(); i++) {
                    int x = eat[i].first;
                    int y = eat[i].second;
 
                    if (dist[x][y] == d) {
                        if (Min.first == x) {
                            if (Min.second > y) {
                                Min = eat[i];
                            }
                        }
                        else if (Min.first > x) {
                            Min = eat[i];
                        }
                    }
                }
            }
            
            cnt++;
            b_x = Min.first;
            b_y = Min.second;
            a[b_x][b_y] = 0;
            ans += dist[b_x][b_y];
            if (s_size == cnt) {
                s_size++;
                cnt = 0;
            }
        }
    }
    
    cout << ans << endl;
 
    return 0;
}

