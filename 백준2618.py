from re import L


N=int(input())
W=int(input())

position=[[0,0]]
position1=[[N-1  ,N-1]]
for _ in range(W):
    i,j=map(int,input().split())
    position.append([i-1,j-1])
    position1.append([i-1,j-1])
dp=[[float('inf') for _ in range(W+1)] for _ in range(W+1)]

#print(position)
dp[0][0]=0
ans=[]
def backtracking(i,j):
    if i==0 and j==0: return
    if j!=1 and j-1==i:
        for k in range(j-1):
            if dp[i][k]==dp[i][j]-(abs(position1[j][0]-position1[k][0])+abs(position1[j][1]-position1[k][1])):
                ans.append(2)
                backtracking(i,k)
    elif i!=1 and i-1==j:
        for k in range(i-1):
            if dp[k][j]==dp[i][j]-(abs(position[i][0]-position[k][0])+abs(position[i][1]-position[k][1])):
                ans.append(1)
                backtracking(k,j)
    elif i<j:
        ans.append(2)
        backtracking(i,j-1)
    elif i>j:
        ans.append(1)
        backtracking(i-1,j)

for i in range(W+1):
    for j in range(W+1):
        if i==j: continue
        if i<j:
            if j!=1 and j-1==i:
                for k in range(j-1):
                    dp[i][j]=min(dp[i][j],dp[i][k]+abs(position1[j][0]-position1[k][0])+abs(position1[j][1]-position1[k][1]))
            else:
                 dp[i][j]=dp[i][j-1]+abs(position1[j][0]-position1[j-1][0])+abs(position1[j][1]-position1[j-1][1])
        else:
            if i!=1 and i-1==j:
                for k in range(i-1):
                    dp[i][j]=min(dp[i][j],dp[k][j]+abs(position[i][0]-position[k][0])+abs(position[i][1]-position[k][1]))
          
            else:
                dp[i][j]=dp[i-1][j]+abs(position[i][0]-position[i-1][0])+abs(position[i][1]-position[i-1][1])

print(position)
print(min(dp[W-1][W],dp[W][W-1]))
if dp[W-1][W]<=dp[W][W-1]: backtracking(W-1,W)
else: backtracking(W,W-1)

for i in dp:
    print(*i)

for i in range(len(ans)-1,-1,-1):
    print(ans[i])
#역추적??

