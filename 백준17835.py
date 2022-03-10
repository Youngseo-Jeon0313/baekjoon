from heapq import *
import sys
input=sys.stdin.readline

n, m, k = map(int,input().split())
adj=[[] for _ in range(n+1)]
hq = []
cost = [float('inf')] *(n+1)
for i in range(m):
    u,v,c =map(int,input().split())
    adj[v].append([u,c])

city=[*map(int,input().split())]
for i in range(k):
    cost[city[i]]=0
    heappush(hq, [0, city[i]])

while hq:
    t, x=heappop(hq)
    if cost[x] != t: continue
    for nx, nt in adj[x]:
        if cost[nx]>t+nt:
            cost[nx]=t+nt
            heappush(hq, [cost[nx],nx])
ans=0
dist=0
for i in range(1, n+1):
    if cost[i]>dist:
        ans=i
        dist=cost[i]

print(ans)
print(dist)