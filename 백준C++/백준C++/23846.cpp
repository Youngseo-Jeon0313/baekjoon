#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include <tuple>
#include <string>
#include <queue>
#include <cmath>
using namespace std;
double pow(float base, int n);

double fac(int n) {
    int res = 1;
    if (n == 0) {
        return 1;
    };
    for (int i = 1; i <= n + 1; i++) {
        res *= i;
    };
    return res;
}

double com(int n, int r) {
    return fac(n) / fac(r) / fac(n - r);
};
    
    


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    double N; int K;
    double ans = 0;
    cin >> N >> K;

    for (int i = 0; i < K; i++) {
        ans += com(N, i);
    }

    ans *= pow(1 / 3, N);
    cout << ans << '\n';

    return 0;
}
