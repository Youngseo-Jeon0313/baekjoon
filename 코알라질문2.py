from sys import stdin

n=7
dp=[[0]*5 for i in range(n)]
dp[0][0]=1
dp[0][1]=8
div=10**9+7

for i in range(1,n):
	
	for j in range(2,5):
		dp[i][j]+=dp[i-1][j-1]*(8-(2*j-2))
		dp[i][j]%=div

	for j in range(5):
		dp[i][j]+=dp[i-1][j]*(j+1)
		dp[i][j]%=div
	
	dp[i][1]+=8

print(sum(dp[-1]))


cnt=0
for i in range(10**(n-1),10**(n)):
	num=str(i)
	if '0' in num:
		continue
	able=True
	for j in range(1,5):
		if str(j) in num and str(9-j) in num:
			able=False
			break
	if not able:
		continue
	cnt+=1

print(cnt)
	