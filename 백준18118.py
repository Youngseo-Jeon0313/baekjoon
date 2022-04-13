import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dp=[[0]*(m) for _ in range(n)]
    for i in range(12):
        if i==10: continue;        
        dp[0][i%m]=i
    
    for i in range(1,n):
        for j in range(m):
                for k in range(11,-1,-1):
                    if k==10: continue
                    if k==11: dp[i][(dp[i-1][j]*100+k)%m]=max(dp[i][(dp[i-1][j]*100+k)%m],dp[i-1][j]*100+k);
                    else:dp[i][(dp[i-1][j]*10+k)%m]=max(dp[i][(dp[i-1][j]*10+k)%m],dp[i-1][j]*10+k);
    print(dp[n-1][0])
#파이썬으로 구현하면 시간초과가 오짐 ㅠㅠㅠ

'''
#include <stdio.h>
#include <string.h>
#include <algorithm>
#define NMAX 10
#define MMAX 100010
using namespace std;
 
int T, N, M;
 
long long int dp[NMAX][MMAX];
 
int main() {
    scanf("%d", &T);
    while(T--) {
        // input
        scanf("%d %d", &N, &M);
 
        // init
        memset(dp, 0, sizeof(dp));
        for(int j=0;j<=11;j++) {
            if(j==10) continue;
            dp[1][j%M] = j;
        }
 
        // dp
        for(int i=1;i<N;i++) {
            for(int j=0;j<M;j++) {
                if(!dp[i][j]) continue;
 
                for(int k=0;k<10;k++) dp[i+1][(j*10+k)%M] = max( dp[i+1][(j*10+k)%M], dp[i][j]*10+k );
                dp[i+1][(j*100+11)%M] = max( dp[i+1][(j*100+11)%M], dp[i][j]*100+11 );
            }
        }
 
        // print
        printf("%lld\n", dp[N][0]);
    }
}
'''