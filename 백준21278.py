from itertools import combinations as cb


N,M=map(int,input().split())
cost=[[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    cost[b][a]=1
    cost[a][b]=1

for i in range(1,N+1):
    cost[i][i]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if cost[i][j] > cost[i][k]+cost[k][j]:
                cost[i][j] = cost[i][k]+cost[k][j]
# print(cost)
ans=float('inf')
ans_1=0; ans_2=0
arr=[i for i in range(1,N+1)]
for x in range(N):
    for y in range(x,N+1):
        # print(i)
        temp=0
        for j in range(1,N+1):
            temp+=min(cost[j][x], cost[j][y])
        if ans>temp: 
            ans_1=x; ans_2=y
            ans=temp;
# print(List)
print(ans_1, ans_2, ans*2)



'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[float('inf') for _ in range(N)] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 2
    graph[b-1][a-1] = 2

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] >graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_time = float('inf')

for i in range(N-1):
    for j in range(i,N):
        chicken1 = i
        chicken2 = j
        sum_time = 0
        for building in range(N):
            sum_time += min(graph[building][chicken1],graph[building][chicken2])
        if max_time > sum_time:
            max_time = sum_time
            max_chicken1 = chicken1
            max_chicken2 = chicken2

print(max_chicken1+1, max_chicken2+1, max_time)


'''