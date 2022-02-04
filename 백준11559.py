from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = 12, 6
arr = list(list(input()) for _ in range(n))
ans = 0

while 1:
    puyo_flag = False
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and arr[i][j] != '.':
                visit[i][j] = 1
                q = deque([(i, j)])
                puyo = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and arr[nx][ny] == arr[i][j]:
                            visit[nx][ny] = 1
                            q.append((nx, ny))
                            puyo.append((nx, ny))
                if len(puyo) >= 4:
                    puyo_flag = True
                    for x, y in puyo:
                        arr[x][y] = '.'
    if puyo_flag == True:ans += 1
    else:break

    for i in range(n - 1):
        for x in range(n - 1):
            for y in range(m):
                if arr[x][y] != '.' and arr[x + 1][y] == '.':
                    arr[x][y], arr[x + 1][y] = '.', arr[x][y]
print(ans)