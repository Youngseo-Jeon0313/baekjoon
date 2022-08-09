N,R,Q=map(int,input().split())
List=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,input().split())
    List[u].append(v)
    List[v].append(u)

visited=[0 for _ in range(N+1)]
subTree=[0 for _ in range(N+1)]

def dfs(node):
    visited[node]=1 #방문 체크
    subTree[node]+=1
    for i in List[node]:
        if not visited[i]:
            dfs(i)
            subTree[node]+=subTree[i]


dfs(R)

print(subTree)

for _ in range(Q):
    n=int(input())
    print(subTree[n])
    
   
