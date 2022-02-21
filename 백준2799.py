#간단한 플러드필 문제
from collections import deque
dr,dc=[1,-1,0,0],[0,0,1,-1]
def floodfill(r,c,star):
    global A,B,C,D,E
    q=deque()
    q.append((r,c))
    check[r][c]=1
    if arr[r][c]=='*': star+=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx, ny=x+dr[i],y+dc[i]
            if check[nx][ny]==0 and arr[nx][ny]!='#':
                if arr[nx][ny]=='*': star+=1
                check[nx][ny]=1
                q.append((nx,ny))
    if star==16: E+=1
    elif star==12:D+=1
    elif star==8:C+=1
    elif star==4:B+=1
    elif star==0: A+=1
A,B,C,D,E=0,0,0,0,0
M,N=map(int,input().split())
arr=list(list(input()) for _ in range(5*M+1))
check=[[0]*(5*N+1) for _ in range(5*M+1)]
for i in range(5*M+1):
    for j in range(5*N+1):
        if arr[i][j]!='#' and check[i][j]==0:
            star=0
            floodfill(i,j,star)
            
print(A,B,C,D,E,sep=' ')