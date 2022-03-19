N,M=map(int,input().split())
cant=list(map(int,input().split()))

dp=[[float('inf')]*106 for _ in range(106)] #dp[day][coupon] 
dp[0][0]=0
for i in range(N+1):
        for j in range(40):
                if dp[i][j]==float('inf'): continue
                result=dp[i][j]
                if i+1 in cant: dp[i+1][j]=min(result, dp[i+1][j]) #뒤가 false라면
                if j>=3: dp[i+1][j-3]=min(result, dp[i+1][j-3]) #쿠폰이 3개 이상이면 써도 됨
                #1일권
                dp[i+1][j]=min(dp[i+1][j],result+10000)
                #3일권
                for k in range(1,4):
                        dp[i+k][j+1]=min(dp[i+k][j+1],result+25000)
                #5일권
                for l in range(1,6):
                        dp[i+l][j+2]=min(dp[i+l][j+2], result+37000)

print(min(dp[N]))
