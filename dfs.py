#DFS 메소드 정의
def dfs(graph, v, visited):
    print(visited)
    #현재 노드를 방문처리
    visited[v] = 1
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#각 노드가 연결된 정보를 표현 (2차원 리스트)
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

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [0] * 9 

dfs(graph, 0, visited)   #출력 : 0 1 3 8 4 5 2 6 7
