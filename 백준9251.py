A=input()
B=input()
dp=[[0]*1001 for _ in range(1001)]
'''
dp로 구현할 수 있는데 
판 때기를 만들어서 사용할 수 있다.
왜?? 여기 관점에서 보는 거랑 저기 관점에서 보는 거랑
다를 수 있기 때문ㅇ
'''
ans=0
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1]==B[j-1]: dp[i][j]=dp[i-1][j-1]+1
        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        ans=max(ans, dp[i][j])
print(ans) #max(dp)