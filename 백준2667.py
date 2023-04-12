from collections import deque

def dfs(start_x,start_y):
    q = deque()
    q.append((start_x,start_y))
    visited[start_x][start_y]=1
    cnt=1
    while q:
        x,y=q.popleft()
        

N=int(input())
Board=[]
for _ in range(N):
    Board.append(list(input()))
visited=[[0 for _ in range(N)] for _ in range(N)]
dfs(0,0)