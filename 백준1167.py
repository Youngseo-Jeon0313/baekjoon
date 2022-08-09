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
Info=[]
for _ in range(n):
    Info.append(list(map(int,input().split())))

for i in range(n):
    for j in range(len(Info[i])-1):
        if j==0:Tree_index=Info[i][j]
        else: 
            if j%2==1:
                Tree[Tree_index].append([Info[i][j],Info[i][j+1]])
#distance ==> 사이클은 없다. 트리가 다익스트라랑 다른 점임 
temp_dist=[-1 for _ in range(n+1)]

def temp_dfs(node, weight):
    for i, j in Tree[node]:
        if temp_dist[i]==-1:
            temp_dist[i]=weight+j
            temp_dfs(i,weight+j)
    return

def dfs(node, weight):
    for i, j in Tree[node]:
        if dist[i]==-1:
            dist[i]=weight+j
            dfs(i,dist[i])
    return

    
ans=0
temp_dist[1]=0; temp_dfs(1, 0) #root노드인 1번 노드부터 시작할 것
temp_index=temp_dist.index(max(temp_dist))


dist=[-1 for _ in range(n+1)]; dist[temp_index]=0
dfs(temp_index,0)

# print(temp_dist)
# print(dist)


print(max(dist))