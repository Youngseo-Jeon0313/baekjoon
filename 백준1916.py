from heapq import *
import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
adj=[[] for _ in range(n+1)]
for i in range(m):
    x,y,t=map(int,input().split())
    adj[x].append([y,t])
    #간선을 인접리스트로 표현해주었다.

s,e=map(int,input().split())

cost=[float('inf')] *(n+1)
#꾸준히 업데이트될 비용 부분 배열
hq=[[0,s]]#cost는 0이고, 입력받은 s부터 시작!
cost[s]=0

while hq:
    t,x=heappop(hq)
    if cost[x]!=t: continue #시간초과 때문??
    for nx, nt in adj[x]:
        if cost[nx]>t+nt:
            cost[nx]=t+nt
            heappush(hq,[cost[nx],nx])

print(cost[e])