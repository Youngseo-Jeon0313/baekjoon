import sys
input=sys.stdin.readline
import heapq
M,N=map(int,input().split())
List=[list(map(int,input().split()))for _ in range(M)]
List_=[[float('inf') for _ in range(N)] for _ in range(M)]
q=[]
heapq.heapify(q)
dx,dy=[-1,1,0,0],[0,0,-1,1]
heapq.heappush(q,[List[0][0],0,0])
List_[0][0]=List[0][0]
while q:
    val,x,y=heapq.heappop(q)
    if List[x][y]==-1: continue
    if List_[x][y]!=val: continue
    for i in range(4):
        nx=x+dx[i]; ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N and List[nx][ny]!=-1:
            if List_[nx][ny]>List_[x][y]+List[nx][ny]:
                List_[nx][ny]=List_[x][y]+List[nx][ny]
                heapq.heappush(q,[List_[nx][ny],nx,ny])

if List_[M-1][N-1]==float('inf'): print(-1)
else:
    print(List_[M-1][N-1])
