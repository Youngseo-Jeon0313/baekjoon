import sys
input=sys.stdin.readline
import heapq

N,M,K,S=map(int,input().split())
P,Q=map(int,input().split())
road=[[] for _ in range(N+1)] #road=[[]]*(N+1) 이거 절대 안 됨 ㅠㅠ
zombie=[int(input()) for _ in range(K)]
for i in range(M):
    a,b=map(int,input().split())
    road[a].append(b)
    road[b].append(a)

def dfs(index,num):
    if num==S: return #이게 더 메모리 적게 씀
    for j in road[index]:
            if not visited[j]:
                visited[j]=1
                dfs(j,num+1)
dp=[float('inf') for _ in range(N+1)]
dp[1]=0
def dijkstra():
    q=[]
    heapq.heappush(q,[0,1])
    while q:
        cost, place=heapq.heappop(q)
        if dp[place]<cost: continue
        for i in road[place]:
            if i in zombie: continue;
            if visited[i] : nextcost=cost+Q
            else: nextcost=cost+P
            if nextcost<dp[i]:
                dp[i]=nextcost
                heapq.heappush(q,[nextcost,i])
    return dp
visited=[0]*(N+1)
for i in zombie: 
    dfs(i,0)
dijkstra()
print(dp)


#다익스트라로 위험구간 표시 + dfs
#다익스트라로 1에서 N으로 가는 숙박비 표현 (DP)
#
