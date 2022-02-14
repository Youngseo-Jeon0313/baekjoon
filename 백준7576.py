'''
시간초과. 굳이 check라는 2차원 배열을 쓰지 않아도 됨
그리고 popleft랑 pop(0)이랑 시간복잡도 차이 존나 남
'''
from collections import deque
M,N=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

def floodfill():
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]==0:
                if arr[nx][ny]==0:
                    arr[nx][ny]=arr[x][y]+1
                    q.append((nx,ny))

dx,dy=[1,-1,0,0],[0,0,1,-1]
q=deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]==1: q.append([i,j]);
floodfill()

max=0; flag=False
for i in range(N):
    for j in range(M):
        if arr[i][j]>max:
            max=arr[i][j]
        if arr[i][j]==0:
            print(-1)
            exit()
print(max-1)