'''
N<=20 그냥 다 해본다.
'''
import sys
input=sys.stdin.readline
from heapq import *

N,D=map(int,input().split())
hq=[]
distance=[float('inf') for _ in range(10000+1)]
graph = [[] for _ in range(10000+1)]

for _ in range(N):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
heappush(hq,(0,0))
distance[0]=0

#이렇게 하고 다시 다익스트라
for i in range(D):
    graph[i].append((i+1,1))

while hq:
    # print(hq)
    dist, now = heappop(hq)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heappush(hq, (cost, i[0]))

# print(distance)
print(distance[D])