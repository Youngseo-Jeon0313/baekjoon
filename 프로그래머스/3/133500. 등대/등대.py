import sys
sys.setrecursionlimit(10 ** 9)

def solution(n, lighthouse):
    adj = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    lights = [[0,1] for _ in range(n+1)]
    
    def dfs(node):
        visited[node]=1
        for adj_node in adj[node]:
            if visited[adj_node]: continue
            dfs(adj_node)
            # 끈 경우 자식노드는 무조건 켜야 함
            lights[node][0] += lights[adj_node][1]
            # 켠 경우 자식노드는 꺼도 되고 켜도 됨
            lights[node][1] += min(lights[adj_node][1], lights[adj_node][0])
    
    for i,j in lighthouse:
        adj[i].append(j)
        adj[j].append(i)
    dfs(1)
    return min(lights[1])