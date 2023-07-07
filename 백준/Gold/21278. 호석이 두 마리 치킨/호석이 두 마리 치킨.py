from itertools import combinations as cb


N,M=map(int,input().split())
cost=[[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    cost[b][a]=1
    cost[a][b]=1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j: cost[i][j]=0
        for k in range(1,N+1):
            if cost[i][j] > cost[i][k]+cost[k][j]:
                cost[i][j] = cost[i][k]+cost[k][j]
# print(cost)
ans=float('inf')
ans_1=0
ans_2=0
arr=[i for i in range(1,N+1)]
for i in cb(arr,2):
    temp=0
    for j in range(1,N+1):
        temp+=min(cost[j][i[0]], cost[j][i[1]])
    if ans>temp: 
        ans_1=i[0]; ans_2=i[1]
        ans=temp; 
print(ans_1, ans_2, ans*2)