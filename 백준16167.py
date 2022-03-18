def dijkstra(s): #출발하는 곳
    cost = [float('inf')]*(n+1)
    hq=[[0,s]]
    cost[s]=0
    while hq:
        t,x=heappop(hq)
        if cost[x]!=t: continue
        for nx, nt in adj[x]:
            if cost[nx]>t+nt:
                cost[nx]=t+nt
                heappush(hq, [cost[nx],nx])
    return cost

from heapq import *
n,r=map(int,input().split())

adj=[[] for _ in range(n+1)]
for i in range(r):
    a,b,c,d,e=map(int,input().split())
    if e<=10: c=c
    else: c+=(e-10)
    adj[a].append([b,c])
