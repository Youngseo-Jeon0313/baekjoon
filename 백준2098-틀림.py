import sys
input=sys.stdin.readline

N=int(input())

List=[]
for _ in range(N):
    List.append(list(map(int,input().split())))

#DP[현재 도시][방문 비트마스킹]=비용
DP=[[float('inf') for _ in range(2**N)] for _ in range(N)]
'''
dfs
파라미터
-비트마스킹
-현재 위치
'''
visited=[0 for _ in range(N)]
ans=float('inf')
def dfs(node,bits):
    global ans
    if bits==2**N-1:
        ans=min(ans,DP[node][bits])
    for i in range(N):
        if List[node][i]!=0 and not bits&(1<<i)   : #안갔으면
            DP[i][bits|1<<i]=min(DP[i][bits|1<<i],DP[node][bits]+List[node][i])
            if not visited[i]: dfs(i,bits|1<<i); visited[i]=1;

DP[0][0]=0
dfs(0,0)

# print(DP)




print(ans)