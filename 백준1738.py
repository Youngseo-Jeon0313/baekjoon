import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수 
edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성
dist = [-float('inf')] * (n+1) # 최장 거리이므로 -무한으로 초기화

# 그래프 생성
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

     
path=[0 for _ in range(n+1)]

# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0
    for i in range(n): # 정점 수만큼 반복
        for j in range(m): # 매 반복 마다 모든 간선 확인
            node = edges[j][0] 
            next_node = edges[j][1] 
            cost = edges[j][2]
            if dist[node] != -float('inf') and dist[next_node] < dist[node] + cost:
                dist[next_node] = dist[node] + cost
                path[next_node]=node #어디에서 왔는지 업뎃될때마다 넣어주기
                if i == n-1: # (간선-1)만큼 돌았는데도 또 돌 경우. 사이클 발생. 그냥 표시를 float('inf)로 해준다.
                    dist[next_node]=float('inf')

# 벨만 포드 알고리즘 수행
bf(1)

if dist[n]==float('inf'): print(-1); exit()
else:
    arr=[n]
    here=n
    while True:
        there=path[here]
        if there==0: break;
        arr.append(there)
        here=there

print(*arr[::-1])