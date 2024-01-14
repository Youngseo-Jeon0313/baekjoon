import heapq
from collections import deque

N, M, A, B = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int,input().split())
    adj[s].append((e,cost))
    adj[e].append((s,cost))
ans = [A,B]
hq = []
road = [[] for _ in range(N+1)] #경로 - index: to / road[index] = from
distance = [float('inf') for _ in range(N+1)]
def dijksta(start):
    distance[start] = 0
    heapq.heappush(hq, [0, start]) #그때까지 걸린 cost, 현재 노드
    while hq:
        now_cost, now_node = heapq.heappop(hq)
        if distance[now_node]<now_cost:
            continue
        for i in adj[now_node]:
            next_node, next_cost = i[0], i[1]
            if now_cost+next_cost < distance[next_node]:
                #print('there', now_cost+next_cost,now_node, distance)
                distance[next_node] = now_cost+next_cost
                road[next_node]=[(now_node)]
                heapq.heappush(hq, [distance[next_node], next_node])
            # 겹치는 곳이 존재한다면 거기에도 넣는다.
            elif now_cost+next_cost == distance[next_node]:
                #print('here',now_node)
                road[next_node].append(now_node)


dijksta(A)
#print(distance)
#print(road)

to_node = B
q = deque([B])
while q:
    to_node = q.popleft()
    ans.append(to_node)
    from_node = road[to_node]
    for node in from_node:
        if node ==A: continue
        q.append(node)

ans = list(set(ans))
ans.sort()
print(len(ans))
print(*ans)


'''
7 10 1 6
1 3 3
1 4 1
4 5 1
5 2 2
2 6 3
1 7 2
7 2 2
3 6 5
4 7 3
3 7 2

'''