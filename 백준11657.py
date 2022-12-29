'''
다익스트라 + 가중치가 음수가 될 수 있을 때

루프를 V-1번 돌리는데, k번째 루프에서는 시작점으로부터 각 정점으로 
k개의 간선을 거쳐서 도달할 수 있는 최단경로를 갱신해주자

*시간 역행 문제가 나올 때 주로 쓰임(음수 때문)
'''


import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수 입력 받기
edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성
dist = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 그래프 생성
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0
    for i in range(n): # 정점 수만큼 반복
        for j in range(m): # 매 반복 마다 모든 간선 확인
            node = edges[j][0] 
            next_node = edges[j][1] 
            cost = edges[j][2] 
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == n-1: # (간선-1)만큼 돌았는데도 또 돌 경우
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)


print(dist)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n+1):
        if dist[i] == INF: 
            print('-1')
        else: 
            print(dist[i])