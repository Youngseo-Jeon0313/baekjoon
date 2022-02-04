def check(x, y):
    if 0 <= x < n and 0 <= y < n: return True
    return False

from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n = int(input())
arr = [[0]* n for _ in range(n)]

student = {}
for i in range(n*n):
    x, s1, s2, s3, s4 = map(int,input().split())
    student[x] = [s1, s2, s3, s4]

for t in student.keys():
    # 좋아하는 학생이 가장 많이 인접한 칸 찾기
    love = [0, deque()]
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                val = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if check(nx, ny) and arr[nx][ny] in student[t]: val += 1
                if val == love[0]: love[1].append((x,y))
                if val > love[0]: love = [val, deque([(x,y)])]
    # 빈칸이 가장 많은 자리 찾기
    blank = [0, []]
    while love[1]:
        x, y = love[1].popleft()
        val = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if check(nx, ny) and arr[nx][ny] == 0:
                val += 1
        if val == blank[0]: blank[1].append((x,y))
        if val > blank[0]: blank = [val, [(x,y)]]
    x, y = blank[1][0]
    arr[x][y] = t
# 점수 구하기
ans = 0
score = [0, 1, 10, 100, 1000]
for x in range(n):
    for y in  range(n):
        val = 0
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if check(nx, ny) and arr[nx][ny] in student[arr[x][y]]: val += 1
        ans += score[val]
print(ans)