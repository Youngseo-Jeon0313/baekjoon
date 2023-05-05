N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for i in range(0, N+1)] for _ in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + A[i-1][j-1]
 
for _ in range(M):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])