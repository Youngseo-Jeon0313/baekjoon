#DFS + Combination(벽을 세울 수 있는 곳을 다 일일히)
from itertools import combinations as cb
from collections import deque
dx, dy=[0,0,1,-1],[1,-1,0,0]
import sys
input=sys.stdin.readline

n, m=map(int,input().split())
arr =[[*map(int,input().split())] for _ in range(n)]
ans=0

wall=[] #빈칸들 중 벽을 선택할 공간
virus=[] #바이러스가 있는 공간
for i in range(n):
    for j in range(m):
        if arr[i][j]==0: wall.append([i,j])
        if arr[i][j]==2: virus.append([i,j])

for w1, w2, w3 in cb(wall,3):
    visit=[[0]*m for _ in range(n)]
    q=deque()
    for x,y in [w1,w2,w3]:
        arr[x][y]=1 #벽으로 선택
    for x,y in virus:
        q.append([x,y])
        visit[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]!=1 and visit[nx][ny]==0:
                visit[nx][ny]=1
                q.append([nx,ny])
    val=0
    #바이러스가 안 번진 곳 탐색
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=1 and visit[i][j]==0:
                val+=1
    ans=max(ans,val)
    #다시 원위치
    for x,y in [w1,w2,w3]:
        arr[x][y]=0

print(ans)