import sys
input=sys.stdin.readline
from heapq import *
INF = int(1e9)

N,E=map(int,input().split())
adj=[[] for _ in range(N+1)]

for _ in range(E):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

A,B=map(int,input().split())

def dijkstra(start, end):
    distance=[INF for _ in range(N+1)]
    distance[start]=0
    hq=[(0,start)]
    while hq:
        cost, node=heappop(hq)
        if cost>distance[node]: continue
        for next_, next_cost in adj[node]:
            if distance[next_]>cost+next_cost:
                distance[next_]=cost+next_cost
                heappush(hq,(cost+next_cost,next_))
    # print(distance)
    return distance[end]

# print(dijkstra(1,A))

answer=(min(
          dijkstra(1,A)+dijkstra(B,N)+dijkstra(A,B),
          dijkstra(1,B)+dijkstra(A,N)+dijkstra(B,A)
          ))
# print(answer)
if answer<INF: print(answer)
else: print(-1)