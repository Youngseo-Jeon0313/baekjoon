N,K=map(int,input().split())
dp=[[0 for col in range(N+1)] for row in range(K+1)]
for i in range(K+1):
    dp[i][0]=1
for k in range(N+1):
    dp[0][k]=1
for i in range(1,K+1):
    for k in range(1,N+1):
        dp[i][k]=dp[i-1][k]+dp[i][k-1]
print(dp[K-1][N]%1000000000)