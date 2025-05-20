def dijkstra(s):
    cost = [float('inf')]*(n+1)
    hq = [[0,s]]
    cost[s]=0
    while hq:
        t,x = heappop(hq)
        if cost[x] != t: continue
        for nx, nt in adj[x]:
            if cost[nx]>t+nt:
                cost[nx]=t+nt
                heappush(hq, [cost[nx],nx])
    return cost

from heapq import *
import sys
input=sys.stdin.readline

n,w,ex = map(int,input().split())
adj = [[] for _ in range(n+1)]
for i in range(w):
    s,e,t=map(int,input().split())
    adj[s].append([e,t])

timeStart = [0]*(n+1)
for i in range(1,n+1):
    time=dijkstra(i)
    timeStart[i]=time[ex]
timeEnd = dijkstra(ex)

print(max(timeStart[i]+timeEnd[i] for i in range(1,n+1)))