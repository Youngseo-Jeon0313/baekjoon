import sys
input=sys.stdin.readline
#bfs dfs 같이 쓰기??
N=int(input())
List=list(map(int,input().split()))
List=[0]+List
friend=[[] for _ in range(N+1)]
for _ in range(N-1):
    x,y=map(int,input().split())
    friend[x].append(y)
    friend[y].append(x)
def dfs_bfs(node, depth, arr,visit):
    visit[node]=1
    global ans
    if depth==N+1: return;
    temp=float('inf'); #print(arr)
    for k in arr: 
        temp=min(temp,List[k])
    if temp*len(arr)>ans:ans=temp*len(arr); depth=len(arr)
    if temp*len(arr)<ans and len(arr)>depth:return;
    for i in friend[node]:
        if not visit[i]: 
            visit[i]=1; 
            dfs_bfs(i,depth,arr+[i],visit)
            visit[i]=0
    for j in friend[i]:
                if visit[i] and not visit[j]:
                    visit[j]=1;
                    dfs_bfs(j,depth, arr+[j],visit)
                    visit[j]=0

ans=0; visit=[0 for _ in range(N+1)];
for i in range(1,N+1):
    visit[i]=1
    dfs_bfs(i,1, [i],visit) #1번 노드부터 해서 함수에서 체크 깊이는 1부터 차례대로 증가시킨다.
    
print(ans)
