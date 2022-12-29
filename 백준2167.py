N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
prefix_sum=[[0 for i in range(0,M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j]=prefix_sum[i][j-1]+prefix_sum[i-1][j]-prefix_sum[i-1][j-1]+A[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y =map(int,input().split())
    print(prefix_sum[x][y]-prefix_sum[x][j-1]-prefix_sum[i-1][y]+prefix_sum[i-1][j-1])
print(prefix_sum)