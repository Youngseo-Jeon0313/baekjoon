'''
dfs
'''
ans = []

def dfs(value, x,y,depth):
    if depth == 6:
        ans.append(value)
        return
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if (0<= next_x) and (next_x < 5) and (0<= next_y) and (next_y < 5):
            
                dfs(value+Board[x+dx[i]][y+dy[i]], x+dx[i], y+dy[i], depth+1)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

Board = []
for _ in range(5):
    Board.append(list(input().split()))

# print(Board)
# 6자리 수의 종류 구하기

for i in range(5):
    for j in range(5):
        dfs('',i,j,0)

# print(set(ans))
print(len(set(ans)))
