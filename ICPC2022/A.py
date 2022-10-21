import sys
input=sys.stdin.readline
from collections import deque

m,n=map(int,input().split())
indegree=[0]*(n+1)
graph = [[]for _ in range(n+1)]

for _ in range(m):
    s,e=map(int,input().split())
    graph[s].append(e)
    indegree[e]+=1
visited=[0 for _ in range(n+1)]
result=[]
queue=deque()
print(indegree)
for j in range(n+1):
    if indegree[j]==0:
        queue.append([j,1])
        visited[j]=1
    while queue:
        current,cnt=queue.popleft()
        result.append(current)
        for i in graph[current]:
            if visited[i]: continue;
            indegree[i]-=1
            visited[i]=max(visited[i],cnt+1)
            if indegree[i]==0:
                queue.append([i,cnt+1])
print(visited)
print(max(visited)+1)