import sys
input=sys.stdin.readline


def flood_fill(check):
    global MAX
    check[i][j] = 1
    q.append((i,j,1))
    while q:
        x, y, z = q.popleft()
        MAX=max(MAX,z)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if Board[nx][ny] and not check[nx][ny]:
                    check[nx][ny] = z+1
                    q.append((nx, ny,z+1))

from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 


N,M=map(int,input().split())
Board=[]
for ___ in range(N):
    Board.append(list(map(int,input().split())))

check = [[0]*M for _ in range(N)]
check2=[[0]*M for _ in range(N)]
check3=[[0]*M for _ in range(N)]
MAX=0
q = deque()
q_=deque()
for i in range(N):
    for j in range(M):
        if check[i][j] == 0 and Board[i][j]:
            flood_fill(check)


for i in range(N):
    for j in range(M):
        if check[i][j]==MAX:
            if check3[i][j]==0 and Board[i][j]:
                flood_fill(check3)


subMAX=0
for i in range(N):
    for j in range(M):
        if check3[i][j]==MAX and not check2[i][j]:
            q_.append((i,j,1))
            check2[i][j]=1
            while q_:
                x_, y_, z_ = q_.popleft()
                if z_==MAX: subMAX=max(subMAX,Board[i][j]+Board[x_][y_])
                for k in range(4):
                    nx, ny = x_ + dx[k], y_ + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if Board[nx][ny] and not check2[nx][ny]:
                            check2[nx][ny] = z_+1
                            q_.append((nx, ny,z_+1))
                print(q_)
print(check)
print(MAX)
print(check3)
print(check2)
print(subMAX)