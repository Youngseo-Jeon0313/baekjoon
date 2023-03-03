#가장 거리가 가까운 것부터 먼 것으로 순서대로 점차 탐색함
#큐를 이용
from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True #while문에 안 들어갈 수도 있으므로 여기서 체크해줘야 하는 거 잊지말자ㅠㅠㅠ제발

graph = [
    [1,2], #0번 노드에서 1과 2로 이동 가능하다.
    [3, 4, 5], #1번 노드에 연결된 건 2,3,8 이다.
    [6,7], #2번 노드에 연결된 건 1,7이다.
    [8],
    [3],
    [],
    [],
    [],
    []
]


visited = [False] * 9

bfs(graph, 0, visited)