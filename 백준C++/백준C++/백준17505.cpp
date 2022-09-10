#include <iostream>
#include <algorithm>

using namespace std;
#define ll long long
ll n, k;
int ans[314166];

int main() {
    cin >> n >> k;
    int s = 1, e = n;
    for (ll i = 1; i <= n; i++) {
        if (k >= n - i) {
            k -= (n - i);
            ans[i] = e--;
        }
        else ans[i] = s++;
    }
    if ((k != 0) || (s <= e)) puts("-1");
    else for (int i = 1; i <= n; i++) printf("%d ", ans[i]);
}
