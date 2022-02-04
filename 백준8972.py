dx, dy = [1, 1, 1, 0, 0, 0, -1, -1, -1], [-1, 0, 1] * 3

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
move = list(map(int, list(input())))
enemy = []
for x in range(n):
    for y in range(m):
        if arr[x][y] == 'I': sx, sy = x, y
        if arr[x][y] == 'R': enemy.append((x, y))

for t in range(len(move)):
    sx, sy = sx + dx[move[t]-1], sy + dy[move[t]-1]
    if (sx, sy) in enemy:
        print("kraj {}".format(t + 1))
        exit(0)

    amount = [[0] * m for _ in range(n)]
    while(enemy):
        x, y = enemy.pop()
        ex, ey = x, y
        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if abs(sx-ex) + abs(sy-ey) > abs(sx-nx) + abs(sy-ny):
                    ex, ey = nx, ny
        amount[ex][ey] += 1
        if sx == ex and sy == ey:
            print("kraj {}".format(t+1))
            exit(0)

    for x in range(n):
        for y in range(m):
            if amount[x][y] == 1: enemy.append((x,y))

arr = [['.']*m for _ in range(n)]
arr[sx][sy] = 'I'
for x, y in enemy:
    arr[x][y] = 'R'

for i in range(n):
    print(''.join(arr[i]))