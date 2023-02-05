import sys
input = sys.stdin.readline

import heapq

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())
INF = int(1e9)

# 그래프 초기화
graph = [[] * (n+1) for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
dp=[0 for _ in range(n+1)]; dp[2]=1
# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

d=INF
ans=0
def dijkstra(start):
    global d; global ans
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # print(q)
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist: continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next,next_dist in graph[now]:
            cost = dist +next_dist
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost,next))
            if dist>distance[next]:
                dp[now]+=dp[next]

# 다익스트라 알고리즘을 수행
dijkstra(2)

# 모든 노드로 가기 위한 최단 거리를 출력
print(dp[1])
