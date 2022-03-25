import heapq
from collections import deque
import sys
input=sys.stdin.readline

N,M,K,S=map(int,input().split())
P,Q=map(int,input().split())
road=[[] for _ in range(N+1)] #road=[[]]*(N+1) 이거 절대 안 됨 ㅠㅠ
zombie=[int(input()) for _ in range(K)]
for _ in range(M):
    a,b=map(int,input().split())
    road[a].append(b)
    road[b].append(a)


def dfs(index):
    dq=deque()
    dq.append([index,0])
    visited[index]=1
    while dq:
        here,num=dq.popleft()
        if num<S:
            for i in road[here]:
                if not visited[i]:
                    visited[i]=1
                    ret[i]=1
                    dq.append([i,num+1])


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
            if ret[i] : nextcost=cost+Q
            else: nextcost=cost+P
            if nextcost<dp[i]:
                dp[i]=nextcost
                heapq.heappush(q,[nextcost,i])
    if ret[N]: return dp[N]-Q
    else: return dp[N]-P

ret=[0]*(N+1)
for i in zombie: 
    visited=[0]*(N+1)
    dfs(i)

print(dijkstra())

#다익스트라로 위험구간 표시 + dfs
#다익스트라로 1에서 N으로 가는 숙박비 표현 (DP)

