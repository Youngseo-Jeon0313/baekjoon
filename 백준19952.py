from collections import deque

t=int(input())
for _ in range(t):
    H,W,O,F,Xs,Ys,Xe,Ye=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(O)]
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    check=[[False]*W for _ in range(H)]
    arr[Xe][Ye]=1
    check[Xs][Ys]=1
    q=deque()
    q.append((Xe,Ye))
    while q:
        for i in range(4):
            x,y=Xe+dx[i],Ye+dy[i]
            if 0<=x<H and 0<=y<W:
                if not check[x][y] and 