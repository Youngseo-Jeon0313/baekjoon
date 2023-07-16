import sys
input = sys.stdin.readline
import heapq

# 정점의 개수 n, 간선의 개수 m
n, start, end = map(int, input().split())
# 시작 정점의 번호
# 무한을 의미하는 INF
INF = int(1e9)
# 그래프 초기화
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
max_distance=[0] * (n+1)
# 간선 정보 입력
for _ in range(n-1):
    a, b, c = map(int, input().split())
    # a->b가 c비용
    graph[a].append((b, c))
    graph[b].append((a, c))
# print(graph)
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start, 0))
    distance[start] = 0

    while q:
        # print(q)
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now, max_ = heapq.heappop(q)
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                max_distance[i[0]] = max(max_, i[1])
                heapq.heappush(q, (cost, i[0], max(max_,i[1])))

# 다익스트라 알고리즘을 수행
dijkstra(start)
# print(distance)
# print(max_distance)
# 모든 노드로 가기 위한 최단 거리를 출력

print(distance[end]-max_distance[end])


'''
다익스트라 주의
1. 간 곳을 또 간다. -> check 해줄 필요 없다.
2. heapq는 최소인 것부터 빠진다.
3. 다익스트라 dist 할당해줄 때? 초반에는 float('inf') 로 초기화한다. 이후에 갱신

'''