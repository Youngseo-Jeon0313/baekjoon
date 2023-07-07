from itertools import combinations as cb


N,M=map(int,input().split())
cost=[[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    cost[b][a]=1
    cost[a][b]=1

for i in range(1,N+1):
    cost[i][i]=0
    for j in range(1,N+1):
        for k in range(1,N+1):
            if cost[i][j] > cost[i][k]+cost[k][j]:
                cost[i][j] = cost[i][k]+cost[k][j]
# print(cost)
ans=float('inf')
ans_1=0; ans_2=0
arr=[i for i in range(1,N+1)]
for x in range(N):
    for y in range(x+1,N+1):
        # print(i)
        temp=0
        for j in range(1,N+1):
            temp+=min(cost[j][x], cost[j][y])
        if ans>temp: 
            ans_1=x; ans_2=y
            ans=temp;
# print(List)
print(ans_1, ans_2, ans*2)