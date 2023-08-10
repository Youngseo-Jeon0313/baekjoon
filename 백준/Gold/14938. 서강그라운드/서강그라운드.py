n,m,r=map(int,input().split())
items=list(map(int,input().split()))
road=[[] for _ in range(n+1)]

#init
floid=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r):
    a,b,l=map(int,input().split())
    floid[a][b]=l
    floid[b][a]=l

for k in range(1,n+1):
    floid[k][k]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            floid[i][j]=min(floid[i][j],floid[i][k]+floid[k][j])

ans=0
for i in range(1,n+1):
    temp=0
    for j in range(1,n+1):
        if floid[i][j]<=m:
            # print('만족?',i,j)
            temp+=items[j-1]
    # print(i,temp)
    ans=max(ans,temp)
print(ans)