N,M=map(int,input().split())
Board=[]
ans=[[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    Board.append(input())
for i in range(N):
    flag=0
    for j in range(M):
        if Board[i][j]=='c':
            a=0; flag=1
            ans[i][j]=0
        else:
            if flag:
                ans[i][j]=flag
                flag+=1
            else:
                ans[i][j]=-1

for i in ans:
    print(*i)
            