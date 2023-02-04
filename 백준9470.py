import sys
input=sys.stdin.readline
from collections import deque
t=int(input())

for _ in range(t):
    ans=0
    T,n,m=map(int,input().split())
    indegree=[0]*(n+1)

    graph = [[]for _ in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1
    check=[[]for _ in range(n+1)]
    
    queue=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append([i,1])
    while queue:
        current=queue.popleft()
        node,turn=current[0],current[1]
        for i in graph[node]:
            indegree[i]-=1
            check[i].append(turn)
            if indegree[i]==0: #0이라는 것은 이미 다 왔다는 것
                check[i].sort()
                turn = check[i][-1]
                for k in check[i]:
                    # print('여기',i,k)
                    if check[i].count(k)>=2: turn=k+1
                    ans=turn
                    queue.append([i,turn])
    print(T,ans)
    
