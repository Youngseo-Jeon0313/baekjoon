N=int(input())
dp=[0 for _ in range(31)]
dp[0]=1; dp[2]=3
for i in range(4,31):
    if i%2==0:
        dp[i]+=dp[i-2]*dp[2]
        for j in range(0,i-2,2):
            dp[i]+=2*dp[j]
    else:
        dp[i]=0
print(dp[N])