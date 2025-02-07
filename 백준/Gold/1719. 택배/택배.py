# 백준 1719

import heapq

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost= map(int,input().split())
    adj[a].append((b,cost))
    adj[b].append((a,cost))


dist_answer = [['' for _ in range(N+1)] for _ in range(N+1)] #여기 다시 살피기
def dijkstra(start):
    dist = [float('inf') for _ in range(N+1)]
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, [0,start,'-']) #cost, curr_node, 가장 먼저 가야 하는 곳
    while hq:
        cost, curr_node, temp_ans = heapq.heappop(hq)
        if cost>dist[curr_node]: continue
        dist[curr_node]=cost
        dist_answer[start][curr_node]=temp_ans
        for next_node, next_cost in adj[curr_node]:
            if dist[next_node]>cost+next_cost:
                if temp_ans=='-':
                    heapq.heappush(hq, [cost+next_cost, next_node, next_node])
                else:
                    heapq.heappush(hq, [cost+next_cost, next_node, temp_ans])
for i in range(1,N+1):
    dijkstra(i)
for i in range(1,N+1):
    for j in range(1,N+1):
        print(dist_answer[i][j], end=' ')
    print()