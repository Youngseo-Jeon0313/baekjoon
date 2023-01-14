import sys
input=sys.stdin.readline


from collections import deque


direction = [(0,1),(1,0),(-1,0),(0,-1)]


N,M=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

ans=0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and L[i][j]==0:
            visited[i][j] = True
            Q = deque([(i,j)])
            if i==0 or j==0 or j==(M-1) or i==(N-1): flag=False; big_flag=True
            while Q:
                y,x = Q.popleft()
                    
                for d in direction:
                    ny = y + d[0]
                    nx = x + d[1]
                    ny = ny%N; nx = nx % M;
                    if  not visited[ny][nx] and L[ny][nx]==0 :
                        visited[ny][nx] = True
                        Q.append((ny,nx))
            ans+=1

print(ans)