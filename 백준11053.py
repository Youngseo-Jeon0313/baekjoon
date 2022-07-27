n=int(input())
A=list(map(int,input().split()))

dp=[1]*n
for i in range(1,n):
    for j in range(i):
        #증가하기만 하면 그냥 일단 넣기
        if A[i]>A[j]: dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
