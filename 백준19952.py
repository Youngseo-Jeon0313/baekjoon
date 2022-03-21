from collections import deque

t=int(input())
for _ in range(t):
    H,W,O,F,Xs,Ys,Xe,Ye=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(O)]
    road=[[0]*W for _ in range(H)]
    for j in arr: road[j[0]-1][j[1]-1]=j[2]
    dx,dy=[-1,0,1,0],[0,-1,0,1]
    check=[[0]*W for _ in range(H)]
    check[Xs-1][Ys-1]=1 #시작점
    q=deque()
    q.append((Xs-1,Ys-1,F))
    arr=[[0]*W for _ in range(H)]
    flag=True
    while q:
        X,Y,f=q.popleft()
        if X==Xe-1 and Y==Ye-1 and F>=0 : flag=False; break;
        if f<=0: continue; #힘이 없어요 못가요ㅠㅠ
        for i in range(4):
            x,y=X+dx[i],Y+dy[i]
            if 0<=x<H and 0<=y<W and not check[x][y]:
                if f>=road[x][y]-road[X][Y]:
                    check[x][y]=1
                    q.append([x,y,f-1])
    if flag==False: print('잘했어!!')
    else: print('인성 문제있어??')

    
