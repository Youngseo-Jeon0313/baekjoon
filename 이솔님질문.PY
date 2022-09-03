def flood_fill():
    global max_dist
    global max_val
    check[i][j]= 1
    q.append((i,j,1))
    while q:
        x,y,z=q.popleft()
        if z>max_dist:max_dist=z; max_val=arr[i][j]+arr[x][y]
        elif z==max_dist:max_val=max(max_val,arr[i][j]+arr[x][y])
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 0 and check[nx][ny] == 0:
                    check[nx][ny] = z+1
                    q.append((nx,ny,z+1))

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
    
from collections import deque
q=deque()
dx,dy=[1,-1,0,0],[0,0,1,-1]
max_dist=1
max_val=0

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            check=[[0]*m for _ in range(n)]
            flood_fill()
# print(max_dist)
print(max_val)