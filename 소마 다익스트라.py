import sys
input=sys.stdin.readline
from heapq import *

N,M=map(int,input().split())
adj=[[] for _ in range(N)]
for i in range(M):
    a,b,cost=map(int,input().split())
    adj[a].append((b,cost))
    adj[b].append((a,cost))
distance=[float('inf') for _ in range(N)]

parking=int(input())
P=[0 for _ in range(N+1)]
for _ in range(parking): P[int(input())]=1

def dijkstra(start):
    distance[start]=0
    index=1
    hq=[(0,start),1,1] #cost, 위치, 차 소유, 차 위치
    while hq:
        cost, node, car_exist, car_pos= heappop(hq)
        #여기 코드 필요함. 만약 목적지를 만났다면??
        
        for next, next_cost in adj[node]:
            #차 가져가서 주차
            if car_exist and P[next]:
                heappush(hq, (cost+next_cost,))
            #차 안 가져감
            #차 가져가서 주차 안함