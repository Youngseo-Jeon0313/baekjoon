#하나의 시작 정점으로 부터 모든 다른 정점까지의 최단 경로
from heapq import *
import sys


direction = [(0,1),(1,0),(-1,0),(0,-1)]

def dijkstra(x,y):
    hq = [[0,x,y]]
    cost[x][y]=0
    while hq:
        c,nx,ny = heappop(hq)
        if cost[nx][ny] != c: continue 
        for dx, dy in direction:
            new_x=nx+dx
            new_y=ny+dy
            if 0<=new_x<n and 0<=new_y<n:
                if cost[new_x][new_y]>c+List[nx][ny]:
                    cost[new_x][new_y]=c+List[nx][ny]
                    heappush(hq, [cost[new_x][new_y],new_x,new_y])
    return cost

index=0
while True:
    index+=1
    n=int(input())
    if n==0: break
    List=[]
    for i in range(n):
        List.append(list(map(int,input().split())))
    cost = [[float('inf')]*n for _ in range(n)] #최소 경로를 찾아야 하므로 inf로 갱신
    dijkstra(0,0)
    print('Problem {0}: {1}'.format(index, cost[n-1][n-1]+List[n-1][n-1]))
