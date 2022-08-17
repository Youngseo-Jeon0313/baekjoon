#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include <tuple>
#include <string>
#include <queue>
using namespace std;
string a;
string b;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int r = 15;

    queue<int> q;


    cin >> a;
    cin >> b;

    for (int i = 0; i < 8; i++) {
        q.push(a[i] - '0');
        q.push(b[i] - '0');
    }
    while (q.size() > 2) {
        for (int i = 0; i < size(q); i++) {
            int t = q.front();
            q.pop();
            q.push((t + q.front()) % 10);
        }
    }

    cout << q.front() << q.back() << '\n';


    return 0;
}
