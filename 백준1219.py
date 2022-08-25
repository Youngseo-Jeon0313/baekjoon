import sys
input = sys.stdin.readline
from collections import deque
N,start,end,M = map(int, input().split()) # 노드 수, 간선 수 
edges = [] 
dist = [-float('inf')]*(N+1) #액수의 최대값을 구해야 하므로

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
money=list(map(int,input().split()))

visited=[0 for _ in range(N+1)]
def check(node):
    visited[node]=1
    q=deque([node])
    while q:
        a=q.pop()
        visited[a]=1
        if a==end: return True
        for i in edges:
            if i[0]==a and not visited[i[1]]:q.append(i[1])
    return False

def bf(start):
    dist[start] = 0
    for i in range(N): # 정점 수만큼 반복
        for j in range(M): # 매 반복 마다 모든 간선 확인
            node = edges[j][0] 
            next_node = edges[j][1] 
            cost = -edges[j][2]+money[edges[j][1]]
            if dist[node] != -float('inf') and dist[next_node] < dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == N-1: # (정점-1)만큼 돌았는데도 또 돌 경우. 사이클 발생. 그냥 표시를 float('inf)로 해준다.
                    #######해당 사이클에서 끝점으로 갈 수 있는지 확인한다.
                    if check(node): print('Gee'); exit(); 
                    else: dist[next_node]=float('inf')
            # print(dist)


bf(start)
# print(dist)

if dist[end]==-float('inf') or dist[end]==float('inf'): print('gg'); 
else:
    print(dist[end]+money[start])

'''
3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000
Gee

'''