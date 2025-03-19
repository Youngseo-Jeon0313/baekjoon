import sys
sys.setrecursionlimit(300000)

answer = 0
def solution(a, edges):
    if sum(a) != 0: return -1
    
    visited=[False for _ in range(len(a))]
    
    adj = [[] for _ in range(len(a))]
    for start,end in edges:
        adj[start].append(end)
        adj[end].append(start)
    
    def dfs(node):
        global answer
        visited[node]=True
        for adj_node in adj[node]:
            if not visited[adj_node]:
                visited[adj_node]=True
                dfs(adj_node)
                a[node]+=a[adj_node]
                answer+=abs(a[adj_node])
    dfs(0)
    
    return answer