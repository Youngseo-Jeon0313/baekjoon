import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

N,K=map(int,input().split())
LEVEL=[[] for _ in range(N+1)]
friends=[[] for _ in range(N+1)] #각각 연결되어있는 노드들을 저장 
invited=[0 for _ in range(N+1)]

for i in range(N-1):
    x,y=map(int,input().split())
    friends[x].append(y)
    friends[y].append(x)

#레벨을 적어주겠다.
def bfs(node,level):
    invited[node]=1
    heapq.heappush(LEVEL[level],[len(friends[node]),node])
    for i in friends[node]:
        if not invited[i]:
            bfs(i,level+1)

bfs(1,0)
# print(LEVEL)

ans=N
for i in range(N,-1,-1):
    while len(LEVEL[i])>K:
        x=heapq.heappop(LEVEL[i])
        for j in LEVEL[i-1]:
            if j[1]==x: j[0]-=1
        ans-=1
print(ans)