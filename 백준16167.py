def dijkstra(s): #출발하는 곳
    cost = [float('inf')]*(n+1)
    hq=[[0,s]]
    cost[s]=0
    while hq:
        t,x=heappop(hq)
        if cost[x]!=t: continue
        for nx, nt in adj[x]:
            if cost[nx]>t+nt :
                cost[nx]=t+nt
                road[nx]=road[x]+1
                heappush(hq, [cost[nx],nx])
            if cost[nx]==t+nt and road[x]+1<road[nx]: 
                road[nx]=road[x]+1
                heappush(hq, [cost[nx],nx])
    return cost

from heapq import *
n,r=map(int,input().split())
adj=[[] for _ in range(n+1)]
road=[0]*(n+1)
road[1]=1
for i in range(r):
    a,b,c,d,e=map(int,input().split())
    if e<=10: c=c
    else: c+=(e-10)*d
    adj[a].append([b,c])
a=dijkstra(1)
if a[n]==float('inf'): print('It is not a great way.')
else: print(a[n], road[n])
#print(dijkstra(1)[r])
