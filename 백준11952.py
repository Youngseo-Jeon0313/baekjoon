import sys
from this import d
input=sys.stdin.readline
import heapq
from collections import deque

N,M,K,S=map(int,input().split())
P,Q=map(int,input().split())
road=[[] for _ in range(N+1)] #road=[[]]*(N+1) 이거 절대 안 됨 ㅠㅠ
zombie=[int(input()) for _ in range(K)]
for _ in range(M):
    a,b=map(int,input().split())
    road[a].append(b)
    road[b].append(a)


def dfs(index,num):
    deque=deque()
    deque.append([index,0])
    while deque:
        
    if num==S: return #이게 더 메모리 적게 씀
    for j in road[index]: #여기서 오류가 나는데 아무래도 A 좀비 영역과 B 좀비 영역이 겹칠 때가 문제가 생기는 것 같다..
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
    if visited[N]: return dp[N]-Q
    else: return dp[N]-P
visited=[0]*(N+1)
for i in zombie: 
    dfs(i,0)
print(dijkstra())

#다익스트라로 위험구간 표시 + dfs
#다익스트라로 1에서 N으로 가는 숙박비 표현 (DP)
#
