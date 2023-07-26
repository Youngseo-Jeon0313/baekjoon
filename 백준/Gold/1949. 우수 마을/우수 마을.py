import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    visited[n]=1
    DP[n][1]=List[n]
    for i in node[n]:
        if visited[i]: continue
        dfs(i) #해당 노드 처리
        #
        DP[n][0]+=max(DP[i][0],DP[i][1])#주변꺼에서 아닌 곳, 또는 주변꺼에서 맞는 곳
        DP[n][1]+=DP[i][0]
        
N=int(input())
List=list(map(int,input().split()))
List=[0]+List
node=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)
DP=[[0 for _ in range(2)] for _ in range(N+1)]

dfs(1)
# print(DP)
print(max(DP[1]))