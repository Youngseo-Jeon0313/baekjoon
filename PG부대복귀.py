#BFS, 단 1에서 시작하여!
from collections import deque



def solution(n, roads, sources, destination):
    adj=[[] for _ in range(n+1)]
    answer=[]
    check=[-1 for _ in range(n+1)]
    
    for i in roads:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    def bfs(start):
        deq=deque([])
        deq.append([start,0])
        check[start]=0
        while deq:
            node,depth=deq.popleft()
            check[node]=depth
            for i in adj[node]:
                if check[i]==-1:
                    check[i]=depth+1
                    deq.append([i,depth+1])
    bfs(destination)
    # print(check)
    for j in sources:
        answer.append(check[j])
    
    return answer