N=int(input())
DP=[[0 for _ in range(10)] for _ in range(N+1)]
DP[0]=[0,1,1,1,1,1,1,1,1,1]
for i in range(1,N):
    for j in range(10):
        if j==0: DP[i][j]=DP[i-1][1]
        elif j==9: DP[i][j]=DP[i-1][8]
        else: DP[i][j]=DP[i-1][j-1]+DP[i-1][j+1]
# print(DP)
a=sum(DP[N-1])
print(a%1000000000)