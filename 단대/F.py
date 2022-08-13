from heapq import *
import sys
input=sys.stdin.readline


def dijkstra(s):
    hq = [[0,s,0]] #비용, 어디, 그때까지의 거리
    cost[s]=0
    print(hq)
    while hq:
        t, x, star = heappop(hq)
        if cost[x] != t: continue #이미 방문했다. 1->5방문인데 1->2->5로 방문했을 경우를 의미
        for nx, nt in adj[x]:
            if star<nt:
                if cost[nx]>t+nt:
                    cost[nx]=t+nt
                    heappush(hq, [cost[nx],nx,nt])
        # print(hq)
    return cost


N,M=map(int,input().split())
adj = [[] for _ in range(N+1)] #어디가 어디로 연결되어 있는가 [~와 연결, 가중치]
for _ in range(M):
    a,b,length=map(int,input().split())
    adj[a].append([b,length])
    adj[b].append([a,length])

start,end=map(int,input().split())
cost = [float('inf')]*(N+1) #최소 경로를 찾아야 하므로 inf로 갱신
dijkstra(start)
if cost[end]==float('inf'): print("DIGESTA");
else:print(cost[end])

