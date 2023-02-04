import sys
input=sys.stdin.readline

#가장 거리가 가까운 것부터 먼 것으로 순서대로 점차 탐색함
#큐를 이용
from collections import deque

ans=0

def bfs(graph, start, visited):
    global ans
    queue=deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        ans+=1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N=int(input())
M=int(input())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M): 
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)



bfs(graph, 1, visited)
# print(visited)
print(ans-1)