#트리에서의 DP/ DFS



import sys
sys.setrecursionlimit(10**9)
#TOP DOWN. bottom up으로는 구현 안된다. 
N=int(input())
friend=[[] for _ in range(N+1)]
for _ in range(N-1):
    x,y=map(int,input().split())
    friend[x].append(y)
    friend[y].append(x)
visited=[0 for _ in range(N+1)]
#init
DP=[[0,0] for _ in range(N+1)]
print(DP)

def dfs(x):
    visited[x]=1
    if len(friend[x])==0: #그냥 노드 1개만 주어질 경우
        DP[x][0]=0
        DP[x][1]=1
    else:
        for i in friend[x]:
            if not visited[i]:
                dfs(i) #관건..!
                DP[x][1]+=min(DP[i][0],DP[i][1])
                DP[x][0]+=DP[i][1]
        DP[x][1]+=1 #없을 땐 무조건 있
dfs(1)
# print(DP)
print(min(DP[1][0], DP[1][1]))

