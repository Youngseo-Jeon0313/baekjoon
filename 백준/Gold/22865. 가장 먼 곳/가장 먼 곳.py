import sys
input = sys.stdin.readline
import heapq

N=int(input())
A,B,C=map(int,input().split())
graph = [[] * (N+1) for _ in range(N+1)]
ans=[0 for _ in range(N+1)]
M=int(input())
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    distance = [float('inf') for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return distance
distance_A = dijkstra(A)
distance_B = dijkstra(B)
distance_C = dijkstra(C)

for i in range(1,N+1):
    ans[i]=min(distance_A[i],distance_B[i], distance_C[i])
# print(ans)
print(ans.index(max(ans)))