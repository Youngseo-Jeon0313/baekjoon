from heapq import *
import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
adj=[[] for _ in range(n+1)]
for i in range(m):
    x,y,t=map(int,input().split())
    adj[x].append([y,t])
s,e=map(int,input().split())

cost=[float('inf')] *(n+1)
hq=[[0,s]]
cost[s]=0

while hq:
    t,x=heappop(hq)
    if cost[x]!=t: continue
    for nx, nt in adj[x]:
        if cost[nx]>t+nt:
            cost[nx]=t+nt
            heappush(hq,[cost[nx],nx])

print(cost[e])