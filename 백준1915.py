
N,M = map(int,input().split())
square= []
for _ in range(N):
    square.append(list(input()))
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
#dp[i][j] : 현재 i,j를 정사각형의 맨 오른쪽 아래로 두었을 때 정사각형의 최대 널비
ans = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if square[i-1][j-1]=='1':
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1 # 왼쪽/위/왼쪽위 중 가장 min값+1
            ans = max(ans,dp[i][j])

print(ans*ans)