t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dp=[[0]*(m) for _ in range(n)]
    for i in range(12):
        if i==10: continue;
        dp[0][i%m]=i
    
    for i in range(1,n):
        for j in range(m):
            if dp[i-1][j] != float('inf'):
                for k in range(12):
                    if k==10: continue
                    elif k==11: 
                        if dp[i][(dp[i-1][j]*100+k)%m]<dp[i-1][j]*100+k:dp[i][(dp[i-1][j]*100+k)%m]=dp[i-1][j]*100+k
                    else: 
                        if dp[i][(dp[i-1][j]*10+k)%m]<dp[i-1][j]*10+k:dp[i][(dp[i-1][j]*10+k)%m]=dp[i-1][j]*10+k
    print(dp[n-1][0])