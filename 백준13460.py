'''
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는가?
10번 이하로 움직여서 빼낼 수 없다면 -1 출력
'''
import sys
from collections import deque


N,M=map(int,input().split()) #세로 가로
List=[]
for _ in range(N):List.append(list(input()))
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if List[i][j]=='R': R_x=i; R_y=j
        elif List[i][j]=='B': B_x=i; B_y=j;
q=deque([])
q.append((R_x,R_y,B_x,B_y,1))
visited[R_x][R_y][B_x][B_y]=True
while True:
    redx,redy,bluex,bluey,num=q.popleft()
    if num>11: print(-1); break; #10번 넘게 돌면 이제 끝.
    for how in range(4):
        if how==0: #밑으로 
            nrx,nry,nbx,nby=redx,redy,bluex,bluey
            while List[nrx+1][nry]!='#' and List[nrx][nry]!='O':
                nrx+=1;
            while List[nbx+1][nby]!='#' and List[nbx][nby]!='O':
                nbx+=1; 
            #만약 겹치면 원래 앞에 있었던 애를 잘 따져가지고
            if List[nbx][nby]!='O' and nrx==nbx and nry==nby:
                if redx < bluex: nrx-=1;
                else : nbx -=1
        elif how==1: #위로
            nrx,nry,nbx,nby=redx,redy,bluex,bluey
            while List[nrx-1][nry]!='#' and List[nrx][nry]!='O':
                nrx-=1; 
            while List[nbx-1][nby]!='#' and List[nbx][nby]!='O':
                nbx-=1; 
            if List[nbx][nby]!='O' and nrx==nbx and nry==nby:
                if redx < bluex: nbx+=1;    
                else: nrx+=1
        elif how==2: #왼쪽으로
            nrx,nry,nbx,nby=redx,redy,bluex,bluey
            while List[nrx][nry-1]!='#' and List[nrx][nry]!='O':
                nry-=1;
            while List[nbx][nby-1]!='#' and List[nbx][nby]!='O':
                nby-=1;
            if List[nbx][nby]!='O' and nrx==nbx and nry==nby:
                if redy < bluey: nby+=1;    
                else: nry+=1
        else: #오른쪽으로
            nrx,nry,nbx,nby=redx,redy,bluex,bluey
            while List[nrx][nry+1]!='#' and List[nrx][nry]!='O':
                nry+=1;
            while List[nbx][nby+1]!='#' and List[nbx][nby]!='O':
               nby+=1;
            if List[nbx][nby]!='O' and nrx==nbx and nry==nby:
                if redy < bluey: nry-=1;   
                else: nby -=1;
        if List[nrx][nry]=='O' and List[nbx][nby]!='O' : print(num); exit();
        else: 
            if not visited[nrx][nry][nbx][nby]: q.append((nrx,nry,nbx,nby,num+1)); visited[nrx][nry][nbx][nby]=True

    if len(q)==0: 
        print(-1); break;