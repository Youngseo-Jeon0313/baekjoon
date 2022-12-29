#하나의 시작 정점으로 부터 모든 다른 정점까지의 최단 경로
from heapq import *
import sys
input=sys.stdin.readline


def dijkstra(s):
    cost = [float('inf')]*(n+1) #최소 경로를 찾아야 하므로 inf로 갱신
    hq = [[0,s]]
    cost[s]=0
    while hq:
        t,x = heappop(hq)
        if cost[x] != t: continue #이미 방문했다. 1->5방문인데 1->2->5로 방문했을 경우를 의미
        #이미 작은 요소로 갱신이 되었기 때문에 다시 볼 필요 없음
        for nx, nt in adj[x]:
            if cost[nx]>t+nt:
                cost[nx]=t+nt
                heappush(hq, [cost[nx],nx])
    return cost


n,w,ex = map(int,input().split())
adj = [[] for _ in range(n+1)] #어디가 어디로 연결되어 있는가
for i in range(w):
    s,e,t=map(int,input().split())
    adj[s].append([e,t])