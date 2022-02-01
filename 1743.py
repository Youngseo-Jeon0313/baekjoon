def flood_fill(x, y):
    global res
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] and not check[nx][ny]:
                res += 1
                check[nx][ny] = 1
                flood_fill(nx,ny)

import sys
sys.setrecursionlimit(10000)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
n, m, k = map(int,input().split())
arr = [[0]*m for _ in range(n)]
for i in range(k):
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1
check = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and check[i][j] == 0:
            res = 1
            check[i][j] = 1
            flood_fill(i, j)
            ans = max(ans, res)
print(ans)