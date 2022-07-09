from collections import deque

N,M,K=map(int,input().split())
DPS=[] #departmentstore
for _ in range(N):
    DPS.append(list(map(int,input().split())))

dolls=[]
check=[[0 for _ in range(M)] for _ in range(N) ]

for i in range(N):
    for j in range(M):
        if DPS[i][j]==3:dolls.append([i,j])
        elif DPS[i][j]==4: x=i; y=j;

dx,dy=[1,-1,0,0],[0,0,1,-1]
q=deque([])
q.append([x,y])
check[x][y]=1
while q:
    tempx,tempy=q.popleft()
    for a in dolls: 
        if abs(tempx-a[0])+abs(tempy-a[1])<=K or DPS[tempx][tempy]==1<=K: continue #거긴 못 가
    for i in range(4):
        nx=tempx+dx[i];ny=tempy+dy[i]
        if 0<=nx and nx<N and 0<=ny and ny<M: 
                if DPS[nx][ny]==1 or DPS[nx][ny]==3 or check[nx][ny] :continue 
                flag=True
                for a in dolls:
                    if abs(nx-a[0])+abs(ny-a[1])<=K : flag=False;continue #거긴 못 가
                if DPS[nx][ny]==2 and flag==True: print(check[tempx][tempy]+1); exit(); 
                if flag==True:check[nx][ny]=check[tempx][tempy]+1
                q.append([nx,ny]); 
print(-1)