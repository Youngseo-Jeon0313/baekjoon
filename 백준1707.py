'''
연결그래프 아닐 때 생각해줘야함
'''
#어떤 노드와 간선으로 연결되어있는 것이 서로 달라야 함.
'''
dfs로 해결가능.

'''
from collections import deque
T=int(input())
for _ in range(T):
    V,E=map(int,input().split())
    List=[[] for _ in range(V+1)]
    visited=[0 for _ in range(V+1)]
    
    flag=True
    for _ in range(E):
        x,y=map(int,input().split())
        List[x].append(y)
        List[y].append(x)
    for i in range(1,V+1):
        if not visited[i]:
            q=deque([i]); visited[i]=1
        while q:
            x=q.popleft();
            for j in List[x]:
                if not visited[j]: visited[j]=-visited[x]; q.append(j)
                else: 
                    if visited[j]==visited[x]: flag=False;
            if flag==False: break;
    
    if flag==False: print('NO')
    else: print('YES')

        
        