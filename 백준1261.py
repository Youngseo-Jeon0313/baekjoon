import sys
input=sys.stdin.readline
from collections import deque

M,N=map(int,input().split())
Board=[]
for _ in range(N):
    Board.append(list(input()))
dx=[-1,1,0,0]; dy=[0,0,-1,1]
q=deque([[0,0,0]])
visited=[[0 for _ in range(M)] for _ in range(N)]


while q:
    x,y,count=q.popleft()
    visited[y][x]=1
    # print(x,y,count)
    if x==M-1 and y==N-1: print(count); exit();
    for i in range(4):
        nx=x+dx[i]; ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if visited[ny][nx]: continue
            if Board[ny][nx]=='0':#갈 수 있다.
                q.appendleft([nx,ny,count])
            else: #벽이 있따.
                q.append([nx,ny,count+1])
        