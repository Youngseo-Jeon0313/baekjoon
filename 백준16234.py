from collections import deque
dr,dc=[1,-1,0,0],[0,0,1,-1]

def floodfill(r,c,LIST):
    #여기서 평균도 다 따져서 바꿔주는 것까지 하기
    global sum
    q=deque(); 
    check[r][c]=1
    q.append((r,c))
    LIST.append((r,c))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dr[i],y+dc[i]
            if 0<=nx<N and 0<=ny<N and check[nx][ny]==0 and abs(arr[nx][ny]-arr[x][y])<=R and L<=abs(arr[nx][ny]-arr[x][y]):
                    check[nx][ny]=1
                    sum+=arr[nx][ny]
                    LIST.append((nx,ny))
                    q.append((nx,ny))
    return LIST,sum


ans=0
N,L,R=map(int,input().split())
arr=list(list(map(int,input().split())) for _ in range(N))

while True:
    flag=False
    check=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not check[i][j]: 
                LIST=[]; 
                sum=arr[i][j]
                floodfill(i,j,LIST)
                if len(LIST)>1:
                    flag=True
                    for a,b in LIST:
                        arr[a][b]=sum//len(LIST)
    if flag==True: ans+=1
    else: break
print(ans)

#주의! floodfill할 때 맨 처음 들어가는 애도 같이 더해줘야 되는거ㅠㅠ