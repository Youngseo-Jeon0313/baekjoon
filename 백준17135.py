from itertools import combinations as cb
from copy import deepcopy

n, m, d = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(n))

Castle = [i for i in range(m)]
Archer = cb(Castle, 3)
ans = 0

for S in Archer:
    arr = deepcopy(MAP)
    kill = 0
    while 1:
        flag = False
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1: flag = True
        if not flag: break

        dist = [d+1]*3
        enemy = [(-1, -1)] * 3

        for j in range(m):
            for i in range(n):
                if arr[i][j] == 1:
                    for k in range(3):
                        ax, ay = n, S[k]
                        ex, ey = i, j
                        if dist[k] > abs(ax - ex) + abs(ay - ey):
                            dist[k] = abs(ax - ex) + abs(ay - ey)
                            enemy[k] = (ex, ey)
        for x, y in enemy:
            if x != -1 and y != -1:
                if arr[x][y] == 1: kill += 1
                arr[x][y] = 0
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if i == 0:
                    arr[i][j] = 0
                    continue
                else: arr[i][j] = arr[i - 1][j]
    ans = max(ans, kill)
print(ans)