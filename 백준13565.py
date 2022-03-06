def floodfill():
    check[0][i]=2
    q.append((0,i))
    while q:
        x, y=q.popleft()
        for k in range(4):
            nx, ny=x+dx[k],y+dy[k]
            if 0<=nx<R and 0<=ny<C:
                if arr[nx][ny]=='0' and check[nx][ny]==0:
                    check[nx][ny]=2
                    q.append((nx,ny))


from collections import deque
dx,dy=[-1,1,0,0],[0,0,-1,1]
q=deque()
R,C=map(int,input().split())
arr=[list(input()) for _ in range(R)]
check=[[0]*C for _ in range(R)]
for i in range(C):
    if check[0][i]==0 and arr[0][i]=='0':
        floodfill()

flag=False
for j in range(C):
    if check[R-1][j]==2:
        flag=True
if flag==False: print('NO')
else: print('YES')