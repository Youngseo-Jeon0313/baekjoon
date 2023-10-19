import sys
input=sys.stdin.readline

from collections import deque
n,m=map(int,input().split())
adj = [[]for _ in range(n)]
real_adj=[[] for _ in range(n)]
#이웃이 몇 개인가 표시
neighbors =[[i,0] for i in range(n)]
neighbors_indextype = [0 for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    neighbors[a][1]+=1
    neighbors[b][1]+=1
    neighbors_indextype[a]+=1
    neighbors_indextype[b]+=1
for i in range(n):
    for j in adj[i]:
        if neighbors_indextype[j]>neighbors_indextype[i]:
            real_adj[i].append(j)
        elif neighbors_indextype[j]<neighbors_indextype[i]:
            real_adj[j].append(i)
visited = [0 for _ in range(n+1)]
neighbors = sorted(neighbors,key = lambda x:x[1])


def bfs(node):
    temp_visited = [0 for _ in range(n)]
    print('node',node)
    deq = deque([])
    deq.append([node, 1])
    while deq:
        _node, depth = deq.popleft()
        print(_node, depth)
        visited[_node]=depth
        temp_visited[_node]=1
        for neighbor in ㅁㅇ[_node] :
            if temp_visited[neighbor] or neighbors_indextype[neighbor]<=depth:continue
            if visited[neighbor]<=depth+1:
                visited[neighbor] = depth+1
                deq.append([neighbor, depth+1])

# 가장 neighbor 수가 작은 것부터 bfs 돌리기 시작

ans = 0
for i in neighbors:
    if not visited[i[0]]:
        bfs(i[0])
        ans = max(ans, max(visited))

print(ans)