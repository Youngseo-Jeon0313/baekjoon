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
        nx,ny=x+dx[i],dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] and not A[nx][ny]:
            A[nx][ny]=val
            val+=1

Bq=deque()
Bq.append((Bx-1,By-1))
B[Bx-1][By-1]=1
val=1
while Bq:
    x,y=Bq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] and not B[nx][ny]:
            B[nx][ny]=val
        val+=1

Cq=deque()
Cq.append((Cx-1,Cy-1))
val=1
CC[Cx-1][Cy-1]=1
while Cq:
    x,y=Cq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] and not CC[nx][ny]:
            CC[nx][ny]=val
            val+=1

print(A)
print(B)
print(CC)
