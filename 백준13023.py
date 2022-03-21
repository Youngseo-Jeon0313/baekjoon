N,M=map(int,input().split())
arr=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(index,num):
    if num==4: print(1); exit();
    for i in arr[index]:
        if not visited[i]:
            visited[i]=1
            dfs(i,num+1)
            visited[i]=0
visited=[0]*N
for i in range(N):
    visited[i]=1
    dfs(i,0)
    visited[i]=0
print(0)
