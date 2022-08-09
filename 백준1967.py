'''
1. 노드 하나 잡고 bfs 한 번해서 가장 먼 노드 a 찾기
2. a 에서 bfs 한 번해서 가장 먼 노드 b 찾기
3. a - b 를 연결하는 경로가 트리의 지름!
'''
import sys
input=sys.stdin.readline
import sys
sys.setrecursionlimit(100000)

n=int(input())
Tree=[[] for _ in range(n+1)] #index는 부모노드 / Tree[index] 속 값은 [자식노드, 가중치] 의미

#distance ==> 사이클은 없다. 트리가 다익스트라랑 다른 점임 
temp_dist=[-1 for _ in range(n+1)]


for _ in range(n-1):
    p,c,w=map(int,input().split())
    Tree[p].append([c,w])
    Tree[c].append([p,w])

def temp_dfs(node, weight):
    for i, j in Tree[node]:
        if temp_dist[i]==-1:
            temp_dist[i]=weight+j
            temp_dfs(i,weight+j)

def dfs(node, weight):
    for i, j in Tree[node]:
        if dist[i]==-1:
            dist[i]=weight+j
            dfs(i,dist[i])
ans=0
temp_dist[1]=0; temp_dfs(1, 0) #root노드인 1번 노드부터 시작할 것
temp_index=max(temp_dist)

for i in range(1,n+1):
    if temp_dist[i]==temp_index:
        dist=[-1 for _ in range(n+1)]; dist[i]=0
        dfs(i,0)
        ans=max(ans, max(dist))

# print(temp_dist)
# print(dist)


print(ans)