from collections import deque
dx,dy = [0,-1,-1,-1,0,1,1,1], [-1, -1, 0, 1, 1, 1, 0, -1]
kx,ky = [-1, -1, 1, 1], [-1, 1, -1, 1]

n, m = map(int,input().split())
arr = list(list(map(int,input().split())) for _ in range(n))
q = deque([(n-1,0), (n-1,1), (n-2,0), (n-2,1)])

for t in range(m):
    d, s = map(int,input().split())
    cq = deque()

    while q:
        x, y = q.popleft()
        nx, ny = (100 * n + x + dx[d - 1] * s) % n, (100 * n + y + dy[d - 1] * s) % n
        arr[nx][ny] += 1
        cq.append((nx, ny))
    not_cloud = list(cq)

    while cq:
        x, y = cq.popleft()
        for i in range(4):
            nx, ny = x + kx[i], y + ky[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                arr[x][y] += 1

    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 2 and (x, y) not in not_cloud:
                q.append((x, y))
                arr[x][y] -= 2

ans = 0
for x in range(n):
    for y in range(n):
        ans += arr[x][y]
print(ans)