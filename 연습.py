def topology_sort():
    result=[]
    queue=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
    while queue:
        current=queue.popleft()
        result.append(current)
        for i in graph[current]:
            