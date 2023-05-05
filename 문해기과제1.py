'''

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 부분합을 미리 구해놓는다
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:  # (1, 1)일 경우
            continue
        elif i == 0:  # 첫 번째 행일 경우
            arr[i][j] += arr[i][j-1]
        elif j == 0:  # 첫 번째 열일 경우
            arr[i][j] += arr[i-1][j]
        else:  # 그 외의 경우
            arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

# 쿼리에 대한 답을 출력한다
for _ in range(m):
    a, b, c, d = map(int, input().split())
    if a == 1 and b == 1:  # (1, 1)일 경우
        print(arr[c-1][d-1])
    elif a == 1:  # 첫 번째 열일 경우
        print(arr[c-1][d-1] - arr[c-1][b-2])
    elif b == 1:  # 첫 번째 행일 경우
        print(arr[c-1][d-1] - arr[a-2][d-1])
    else:  # 그 외의 경우
        print(arr[c-1][d-1] - arr[c-1][b-2] - arr[a-2][d-1] + arr[a-2][b-2])

'''

N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for i in range(0, N+1)] for _ in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + A[i-1][j-1]
 
for _ in range(M):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])