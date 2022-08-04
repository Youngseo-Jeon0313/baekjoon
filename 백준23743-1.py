from heapq import *
import sys
input=sys.stdin.readline

def dijkstra(s,exitdoor):
    hq = [[0,s]]
    cost[s]=0
    last=0
    while hq:
        t,x = heappop(hq)
        if cost[x] != t: continue
        for nx, nt in adj[x]:
            exitdoor=min(exitdoor,List[nx])
            if cost[nx]>t+nt:
                cost[nx]=t+nt
                last=max(cost[nx],last)
                heappush(hq, [cost[nx],nx])
    return [last,exitdoor]



N,M=map(int,input().split())
adj = [[] for _ in range(N+1)]
parent=[i for i in range(N+1)]
cost = [float('inf')]*(N+1)

for _ in range(M):
    a,b,c=map(int,input().split())
    adj[a].append([b,c])

List=list(map(int,input().split()))
List=[0]+List

check=[0 for _ in range(N+1)]
MIN=float('inf')
ans=0
for i in range(1,N+1):
    if cost[i]!=float('inf'): continue
    else:
        time,exitdoor=dijkstra(parent[i],List[i])
        check[parent[i]]=1
    ans+=(time+exitdoor)
print(ans)