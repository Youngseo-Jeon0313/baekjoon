n=int(input())
dp=[0]*(n+1)
dp[1]=1; dp[2]=2; dp[3]=1
for i in range(4, n+1):
    if dp[i-1]==2 or dp[i-3]==2: dp[i]=1
    else: dp[i]=2
if dp[n]==1: print('SK')
else: print('CY')