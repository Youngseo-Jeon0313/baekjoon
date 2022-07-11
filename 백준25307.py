###시간초과 시바ㅣㅏㄹ이러니ㅏ어린아ㅓㄹ


import sys
input=sys.stdin.readline
from collections import deque
dx,dy=[1,-1,0,0],[0,0,1,-1]
N,M,K=map(int,input().split())
DPS=[] #departmentstore
for _ in range(N):
    DPS.append(list(map(int,input().split())))

dolls=deque([])
check=[[0 for _ in range(M)] for _ in range(N)]
no=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if DPS[i][j]==3:dolls.append([i,j]); no[i][j]=1;
        elif DPS[i][j]==4: x=i; y=j;



while dolls:    
    tmpx,tmpy=dolls.popleft()
    for i in range(4):
        nx=tmpx+dx[i]; ny=tmpy+dy[i];
        if  0<=nx and nx<N and 0<=ny and ny<M and no[tmpx][tmpy]<=K and not no[nx][ny] :
            no[nx][ny]=no[tmpx][tmpy]+1
            dolls.append([nx,ny])



q=deque([])
q.append([x,y])
check[x][y]=1
while q:
    tempx,tempy=q.popleft()
    if check[tempx][tempy]>0 and (tempx!=x or tempy!=y) and no[tempx][tempy]: check[tempx][tempy]=-1; continue #거긴 못 가
    for i in range(4):
        nx=tempx+dx[i];ny=tempy+dy[i]
        if 0<=nx and nx<N and 0<=ny and ny<M: 
                if DPS[nx][ny]==1 or DPS[nx][ny]==3 or check[nx][ny] :continue 
                flag=True
                if no[nx][ny] : flag=False; continue #거긴 못 가
                if DPS[nx][ny]==2 :
                    if flag==True: print(check[tempx][tempy]); exit(); 
                if flag==True:check[nx][ny]=check[tempx][tempy]+1; q.append([nx,ny]);
    # print('여깃다!!') 
    # for i in check:
    #     print(*i)
    # print('q는 이래')
    # print(q)
print(-1)


