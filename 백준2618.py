import sys
input=sys.stdin.readline

N=int(input())
W=int(input())

position=[[0,0]]
position1=[[N-1  ,N-1]]
for _ in range(W):
    i,j=map(int,input().split())
    position.append([i-1,j-1])
    position1.append([i-1,j-1])
dp=[[float('inf') for _ in range(W+1)] for _ in range(W+1)]
dp_trace=[[0 for _ in range(W+1)] for _ in range(W+1)] #어디에서 왔니
#print(position)
dp[0][0]=0
ans=[]

#O(W^3)
for i in range(W+1):
    for j in range(W+1):
        if i==j: continue
        if i<j:
            if i and j-1==i:
                for k in range(j-1):
                    if dp[i][j]>dp[i][k]+abs(position1[j][0]-position1[k][0])+abs(position1[j][1]-position1[k][1]):
                        dp[i][j]=dp[i][k]+abs(position1[j][0]-position1[k][0])+abs(position1[j][1]-position1[k][1])
                        dp_trace[i][j]=k
            else:
                dp[i][j]=dp[i][j-1]+abs(position1[j][0]-position1[j-1][0])+abs(position1[j][1]-position1[j-1][1])
                dp_trace[i][j]=j-1
        else:
            if j and i-1==j:
                for k in range(i-1):
                    if dp[i][j]>dp[k][j]+abs(position[i][0]-position[k][0])+abs(position[i][1]-position[k][1]):
                        dp[i][j]=dp[k][j]+abs(position[i][0]-position[k][0])+abs(position[i][1]-position[k][1])
                        dp_trace[i][j]=k
            else:
                dp[i][j]=dp[i-1][j]+abs(position[i][0]-position[i-1][0])+abs(position[i][1]-position[i-1][1])
                dp_trace[i][j]=i-1
# for i in dp:
#     print(*i)
compare=float('inf')
I,J=0,0
#O(W^2)
for i in range(W):
    if dp[i][W]<compare: I,J = i,W; compare=dp[i][W]
    if dp[W][i]<compare: I,J = W,i; compare= dp[W][i]

# print('I랑 J',I,J)
# print(dp_trace)
print(dp[I][J])
for i in range(W):
    if J>I:
        J=dp_trace[I][J]
        ans.append(2)
    else:
        I=dp_trace[I][J]
        ans.append(1)
for i in range(W-1,-1,-1):
    print(ans[i])
#역추적??
