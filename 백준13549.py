from heapq import *
import sys
input=sys.stdin.readline
cost = [float('inf')]*(100000*2+2+1) #최소 경로를 찾아야 하므로 inf로 갱신

def dijkstra(s):
    hq = [[0,s]] #시간, 위치
    cost[s]=0
    while hq:
        # print(hq)
        t,x = heappop(hq)
        if cost[x] != t or x>100000 or x<0: continue #이미 방문했다. 1->5방문인데 1->2->5로 방문했을 경우를 의미
        if cost[x+1]>t+1:
            cost[x+1]=t+1
            heappush(hq, [cost[x+1],x+1])
        if cost[x-1]>t+1:
            cost[x-1]=t+1
            heappush(hq, [cost[x-1], x-1])
        if cost[2*x]>t:
            cost[2*x]=t
            heappush(hq, [cost[2*x], 2*x])
    return cost

#배열 만들기
Subin,Sister=map(int,input().split())
dijkstra(Subin)
print(cost[Sister])
