from collections import deque

dx,dy=[-1,0,1,0],[0,-1,0,1]
R,C=map(int,input().split())
arr=[list(map(int,input())) for _ in range(R)]

A=[[0]*C for _ in range(R)]
B=[[0]*C for _ in range(R)]
CC=[[0]*C for _ in range(R)]
Ax,Ay=map(int,input().split())
Bx,By=map(int,input().split())
Cx,Cy=map(int,input().split())

Aq=deque(); 
Aq.append((Ax-1,Ay-1))
A[Ax-1][Ay-1]=1
val=1
while Aq:
    x,y=Aq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] and not A[nx][ny]:
            A[nx][ny]=A[x][y]+1
            Aq.append((nx,ny))
    val+=1

Bq=deque()
Bq.append((Bx-1,By-1))
B[Bx-1][By-1]=1
val=1
while Bq:
    x,y=Bq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] and not B[nx][ny]:
            B[nx][ny]=B[x][y]+1
            Bq.append((nx,ny))
    val+=1
Cq=deque()
Cq.append((Cx-1,Cy-1))
val=1
CC[Cx-1][Cy-1]=1
while Cq:
    x,y=Cq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] and not CC[nx][ny]:
            CC[nx][ny]=CC[x][y]+1
            Cq.append((nx,ny))
            

root=float('inf')
for i in range(R):
    for j in range(C):
        if A[i][j] and B[i][j] and CC[i][j]:
            root=min(root,max(A[i][j],B[i][j],CC[i][j])-1)
if root==float('inf'): print(-1); exit();
print(root)
sum=0
for i in range(R):
    for j in range(C):
        if A[i][j] and B[i][j] and CC[i][j] and max(A[i][j], B[i][j], CC[i][j])-1==root:
            sum+=1
print(sum)