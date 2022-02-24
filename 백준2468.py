from collections import deque
dx, dy=[1,-1,0,0],[0,0,1,-1]

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
ans =1

for rain in range(1, 101):
    visit =[[0]*n for _ in range(n)]
    val =0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0 and arr[i][j]>rain:
                val+=1
                visit[i][j]=1
                q=deque(); q.append([i,j])
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx, ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and visit[nx][ny] ==0 and arr[nx][ny]>rain:
                            visit[nx][ny]=1
                            q.append([nx,ny])
        ans=max(ans,val)
print(ans)