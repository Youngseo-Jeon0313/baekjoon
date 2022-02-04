from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, L, R = map(int,input().split())
arr = list(list(map(int,input().split())) for _ in range(n))
t = 0 # 추가

while 1:
    visit = [[0]*n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                q = deque(); q.append((i,j))
                visit[i][j] = 1
                union = [(i,j)]
                population = arr[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                            q.append((nx,ny))
                            visit[nx][ny] = 1
                            union.append((nx,ny))
                            population += arr[nx][ny]
                if len(union) > 1:
                    flag = True
                    for x, y in union:
                        arr[x][y] = population // len(union)
    # 추가
    if flag: t += 1
    else: break

print(t)