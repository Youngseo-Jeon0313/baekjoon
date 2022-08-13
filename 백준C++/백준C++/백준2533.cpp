#include <bits/stdc++.h>
using namespace std;

int dp[1000001][2];
vector<int> friends[1000001];
bool visited[1000001]={0};

void dfs(int n) {
    visited[n] = 1;//방문을 했다.
    dp[n][1] = 1;
    for (int j = 0; j < friends[n].size(); j++) {
            int child = friends[n][j];
            if (visited[child])continue;
            dfs(child);
            dp[n][1] += min(dp[child][0], dp[child][1]);
            dp[n][0] += dp[child][1];
        };
};


int main() {
    std::ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int N;
    cin >> N;
    for (int i = 1; i <= N-1; i++) {
        int x; int y;
        cin >> x >> y;
        friends[x].push_back(y);
        friends[y].push_back(x);
    }

    dfs(1);

    cout << min(dp[1][0], dp[1][1]);
    return 0;
}