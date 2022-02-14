#val 쓰는 거 아니지ㅠㅠㅠㅠ
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(input())


def floodfill(r,c):
    check[r][c]=1
    q.append((r,c))
    while q:
        x,y=q.pop(0)
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]=='1' and check[nx][ny]==0:
                check[nx][ny]=check[x][y]+1
                q.append((nx,ny))
dx,dy=[1,-1,0,0],[0,0,1,-1]
q=[]
check=[[0]*M for _ in range(N)]
floodfill(0,0)
print(check[N-1][M-1])
